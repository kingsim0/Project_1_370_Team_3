import time
from my_actor import MyActor
from my_actor import Coordinator

if __name__ == '__main__':
    # Start the actor
    actor_ref = MyActor.start()

    # Send a message to the actor
    actor_ref.tell({'msg': 'Hello from main!'})

    # Start and use the coordinator which interacts with the worker
    coordinator = Coordinator.start()
    coordinator.tell('start')
    
    # Give some time for the message to be processed
    time.sleep(3)

    # Stop all actors
    actor_ref.stop()
    coordinator.stop()