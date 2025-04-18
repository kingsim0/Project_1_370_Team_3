import random
import pykka

# === Basic Actor ===
class MyActor(pykka.ThreadingActor):
    def on_receive(self, message):
        print(f"MyActor received message: {message}")

# === Worker Actor (handles tasks) ===
class Worker(pykka.ThreadingActor):
    def __init__(self, worker_id):
        super().__init__()
        self.worker_id = worker_id

    def on_receive(self, message):
        if isinstance(message, dict) and 'task' in message:
            task = message['task']
            result = f"Worker-{self.worker_id} completed task: {task}"
            sender = message.get('sender')
            if sender:
                sender.tell({'result': result})


# === Coordinator Actor (distributes tasks) ===
class Coordinator(pykka.ThreadingActor):
    def __init__(self, num_workers=3):
        super().__init__()
        self.workers = [Worker.start(worker_id=i) for i in range(num_workers)]
        self.next_worker = 0
        self.num_workers = num_workers

    def on_receive(self, message):
        if message == 'start':
            print("Coordinator: Starting task delegation...")
            for i in range(5):
                task = f"Task-{i+1}"
                self.distribute_task(task)
        elif isinstance(message, dict) and 'result' in message:
            print(f"Coordinator received: {message['result']}")

    def distribute_task(self, task):
        worker = self.workers[self.next_worker]
        worker.tell({'task': task, 'sender': self.actor_ref})
        self.next_worker = (self.next_worker + 1) % self.num_workers
