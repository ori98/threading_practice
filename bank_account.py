from threading import Thread, Lock
from time import sleep

# Shared balance
bal = 100

# Lock object
lock = Lock()


def withdraw(amount: int = 70):
    global bal
    try:
        print(f"Initial balance is: {bal}")
        bal = bal - amount
        # Adding transaction delay
        sleep(3)

        if bal < 0:
            raise ValueError(f"Not Enough balance {bal}")

        # Print the current balance
        print(f"Withdraw SUCCESS! Current balance is: {bal}")
    except ValueError as e:
        print(e)
        # Restoring the balance  to initial amount
        bal += bal + amount


def safe_withdraw(amount: int = 80):
    global bal
    try:
        print("Acquiring lock")
        with lock:
            print("Lock acquired")
            print(f"Initial balance is: {bal}")
            bal = bal - amount
            # Adding transaction delay
            sleep(3)

            if bal < 0:
                raise ValueError(f"Not Enough balance {bal}")

            # Print the current balance
            print(f"Current balance is: {bal}")
    except ValueError as e:
        print(e)
        # Restoring the balance  to initial amount
        bal = bal + amount


# Two people (threads)
p1 = Thread(target=withdraw)
p2 = Thread(target=withdraw)


# Both withdraw
p1.start()
p2.start()

p1.join()
p2.join()

# Reset balance
bal = 100

# Now we try the same with safe_withdraw
p1 = Thread(target=safe_withdraw)
p2 = Thread(target=safe_withdraw)

# Both safe withdraw
p1.start()
p2.start()

p1.join()
p2.join()
