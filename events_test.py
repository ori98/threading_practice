from threading import Thread, Event
from time import sleep


def host_thread(event):
    print("HOST is starting event. Please wait")
    sleep(5)
    event.set()


def attendee_thread(event, attendee_id: int):
    print(f"Attendee {i + 1} is waiting")
    event.wait()
    print(f"Attendee {i + 1} is CHEERING")


if __name__ == "__main__":
    print("Event CREATED")
    event = Event()

    host = Thread(target=host_thread, args=(event,))

    # Spawning 5 attendees
    attendee = [None] * 5
    for i in range(5):
        attendee[i] = Thread(target=attendee_thread, args=(event, i))
        attendee[i].start()

    # Starting the event
    host.start()

    # Joining all the attendee threads
    for i in range(5):
        attendee[i].join()

    host.join()

    print("Event ENDED")
