
# Dynamic Actor Model in Python using Pykka

This project demonstrates the use of the **Actor Model** in Python using the [Pykka](https://www.pykka.org/) library. It includes examples of basic message passing, advanced actor communication, and dynamic task distribution using multiple worker actors.

---

## Files

### `my_actor.py`
Contains all the actor definitions:
- `MyActor`: A basic actor that prints any message it receives.
- `Worker`: Processes tasks assigned by the coordinator.
- `Coordinator`: Manages multiple workers and distributes tasks among them dynamically.

### `main.py`
Runs the actor system:
- Sends a message to `MyActor`
- Starts the `Coordinator` and initiates task delegation to workers

---

## How to Run

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Script**:
   ```bash
   python main.py
   ```

---

## How It Works

### Actors

#### `MyActor`
- A simple actor that logs received messages.

#### `Worker`
- Receives a task and simulates processing.
- Sends the result back to the `Coordinator`.

#### `Coordinator`
- Starts a pool of workers.
- Distributes tasks to them using a round-robin algorithm.
- Receives and logs results from workers.

---

## Sample Output

```
MyActor received message: {'msg': 'Hello from main!'}
Coordinator: Starting task delegation...
Coordinator received: Worker-0 completed task: Task-1
Coordinator received: Worker-1 completed task: Task-2
Coordinator received: Worker-2 completed task: Task-3
Coordinator received: Worker-0 completed task: Task-4
Coordinator received: Worker-1 completed task: Task-5
```

---

## Features

- Round-robin task distribution
- Asynchronous message passing
- Scalable actor-based architecture

---

## Ideas for Expansion

- Add task queues
- Load balancing strategies
- Actor supervision and retry logic
- Remote actor support

---

## License

This project is for educational purposes.
