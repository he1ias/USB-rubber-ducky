import time
from pynput import keyboard

LOG_FILE = "./snake-win.txt"
DELAY = 0.00005

start = time.perf_counter()

controller = keyboard.Controller()

def parse(token):
    if len(token) > 2 and token.startswith("[") and token.endswith("]"):
        return getattr(keyboard.Key, token[1:-1].lower())
    return token

with open(LOG_FILE) as file:
    lines = file.read().split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]

        print(f"[{i}] {line}")

        if not line:
            i += 1
            continue

        action, token = line[0], line[1:]

        try:
            token, target = token.split()
            target = float(target)
        except:
            target = 0.0

        key = parse(token)

        s = start + target - time.perf_counter()
        if s > 0:
            time.sleep(s)

        if action == "+":
            controller.press(key)
        elif action == "-":
            controller.release(key)
        elif action == "#":
            # sleep for 'token' milliseconds
            time.sleep(int(token) / 1000)
        elif action == "@":
            # goto line 'token' (1-indexed) and run it immediately
            goto = int(token)
            start += target - float(lines[goto - 1].split()[1])
            i = goto - 1
            continue

        i += 1

print("Done.")