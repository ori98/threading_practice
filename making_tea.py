from threading import Thread, Condition
from time import sleep

# Condition object
condition = Condition()

# Shared resource
water_ready: bool = False


def boil_water():
    global water_ready
    with condition:
        # First we boil the water and then notify
        print("Boiling water...")
        sleep(3)
        print("Water is ready")
        water_ready = True
        condition.notify()


def make_tea():
    global water_ready
    with condition:
        # Wait for the water to be ready
        while not water_ready:
            condition.wait()

        # Once it is ready, we make tea
        print("Making tea with hot water...")


t1 = Thread(target=boil_water)
t2 = Thread(target=make_tea)

t1.start()
t2.start()

t1.join()
t2.join()
