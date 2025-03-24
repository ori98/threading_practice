import threading
from time import sleep


def create_sys_log():
    for i in range(10):
        sleep(1)
        print(f"System log: {i + 1}")


def create_app_log():
    for i in range(5):
        sleep(1)
        print(f"Application log: {i + 1}")


sys_log_thread = threading.Thread(target=create_sys_log, daemon=True)
app_log_thread = threading.Thread(target=create_app_log)

sys_log_thread.start()
app_log_thread.start()


# sys_log_thread.join()
# app_log_thread.join()

print("FIN")
