# README.md

## Dynamic Actor System in Python using Pykka

This project demonstrates an actor-based system in Python using the **Pykka** library. It showcases asynchronous message passing, task delegation, and actor coordination through a pool of task workers.

###  Files Included
- **main.py**: Entry point that initializes the system.
- **my_actor.py**: Contains actor definitions:
  - `MyActor`: A simple logger actor.
  - `TaskWorker`: Simulates work on tasks.
  - `TaskDispatcher`: Assigns tasks using a round-robin strategy.
- **requirements.txt**: Python dependencies.
- **Dockerfile**: For containerizing the app.

###  How to Run

**1. Install dependencies locally:**
```bash
pip install -r requirements.txt
```

**2. Run the program:**
```bash
python main.py
```

###  Docker Usage
**1. Build the Docker image:**
```bash
docker build -t actor-app .
```

**2. Run the Docker container:**
```bash
docker run --rm actor-app
```

###  How It Works
- **MyActor** logs a simple hello message.
- **TaskDispatcher** creates a pool of 3 **TaskWorker** actors.
- Tasks are sent in round-robin order to workers.
- Workers process tasks and report results back to the dispatcher.

###  Features
- Asynchronous message-based concurrency
- Scalable task delegation
- Round-robin load balancing
- Dockerized setup for portability

### Possible Enhancements
- Add persistent task queues
- Retry mechanism on failure
- Support remote/distributed actors
- Monitoring and metrics dashboard
