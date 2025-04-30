from pykka import ThreadingActor
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ============================
# Actor Definitions (my_actor.py)
# ============================

class MyActor(ThreadingActor):
    def on_receive(self, message):
        logging.info(f"MyActor received message: {message}")


class TaskWorker(ThreadingActor):
    def __init__(self, name, dispatcher):
        super().__init__()
        self.name = name
        self.dispatcher = dispatcher

    def on_receive(self, message):
        task = message.get("task")
        if task:
            time.sleep(1)  # Simulate task processing
            result = f"{self.name} completed task: {task}"
            self.dispatcher.tell({"result": result})


class TaskDispatcher(ThreadingActor):
    def __init__(self):
        super().__init__()
        self.workers = []
        self.next_worker = 0

    def on_start(self):
        logging.info("TaskDispatcher: Starting task delegation...")
        for i in range(3):
            worker = TaskWorker.start(name=f"Worker-{i}", dispatcher=self.actor_ref)
            self.workers.append(worker)

        # Submit 6 tasks
        for i in range(6):
            self.delegate_task(f"Task-{i+1}")

    def delegate_task(self, task):
        worker = self.workers[self.next_worker]
        worker.tell({"task": task})
        self.next_worker = (self.next_worker + 1) % len(self.workers)

    def on_receive(self, message):
        result = message.get("result")
        if result:
            logging.info(f"TaskDispatcher received: {result}")


# ============================
# Main (main.py)
# ============================

if __name__ == '__main__':
    import pykka

    # Start MyActor and send a basic message
    actor = MyActor.start()
    actor.tell({"msg": "Hello from main!"})

    # Start TaskDispatcher which manages TaskWorkers
    dispatcher = TaskDispatcher.start()

    # Let the system run for a bit before shutting down
    time.sleep(7)
    pykka.ActorRegistry.stop_all()
