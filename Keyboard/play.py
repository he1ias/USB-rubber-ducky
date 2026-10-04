import time
from pynput import keyboard

LOG_FILE = "./log.txt"
DELAY = 0.00005

controller = keyboard.Controller()

def parse(token):
    if len(token) > 2 and token.startswith("[") and token.endswith("]"):
        return getattr(keyboard.Key, token[1:-1].lower())
    return token

print("Starting in 1 second... click into the target window.")
time.sleep(1)

with open(LOG_FILE) as file:
    for line in file:
        line = line.rstrip("\n")
        if not line:
            continue

        action, token = line[0], line[1:]
        key = parse(token)

        if action == "+":
            controller.press(key)
        elif action == "-":
            controller.release(key)
        elif action == "#":
            # sleep for 'token' milliseconds
            time.sleep(int(token) / 1000)

        time.sleep(DELAY)

print("Done.")