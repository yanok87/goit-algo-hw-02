"""This module contains a CLI"""

from queue import Queue
import time


def parse_input(user_input):
    """This function parses user input"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Створити чергу заявок
queue = Queue()


# Функція
def generate_request(command):
    """This func creates a request and adds it to the queue"""

    request_id = str(hash(command))[1:13]
    new_request = {"id": request_id, "request": command}
    queue.put(new_request)


# Функція
def process_request():
    """This func processes a request and empties the queue"""

    while not queue.empty():
        time.sleep(1)
        request_in_process = queue.get()
        print(
            f"Processing request #{request_in_process["id"]}, request: {request_in_process["request"]}"
        )
    time.sleep(1)
    print("No requests in the queue")


def main():
    """This function interacts with user and processes the requests"""

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Create request: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "good bye"]:
            print("Good bye!")
            break
        elif command == "process":
            process_request()
        else:
            generate_request(command)
            print("Generating request")


if __name__ == "__main__":

    main()
