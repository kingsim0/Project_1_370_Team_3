# main.py

from pykka import ActorRegistry
import time
from my_actor import MyActor, TaskDispatcher

if __name__ == '__main__':
    # Start MyActor and send a basic message
    actor = MyActor.start()
    actor.tell({"msg": "Hello from main!"})

    # Start TaskDispatcher which manages TaskWorkers
    dispatcher = TaskDispatcher.start()

    # Let the system run for a bit before shutting down
    time.sleep(7)
    ActorRegistry.stop_all()
