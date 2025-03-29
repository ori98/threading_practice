from time import sleep
from threading import Thread, Semaphore

# Only 3 cars are allowed to charge
semaphore_obj = Semaphore(value=3)


def charge_car(car_id: int):
    print(f"Docking: car {car_id}")
    with semaphore_obj:
        print(f"Charging car {car_id}")
        # Time to charge a car
        sleep(5)
        print(f"{car_id} CHARGED")


# Thread of 5 cars
car = [None] * 5

# Spawning threads for car
for i in range(0, 5):
    car[i] = Thread(target=charge_car, args=(i,))

# Sending them to charge
for i in range(0, 5):
    car[i].start()

# Joining all threads
for i in range(0, 5):
    car[i].join()
