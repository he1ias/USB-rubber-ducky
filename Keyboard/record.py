from pynput import keyboard

LOG_FILE = "log.txt"

pressed = []

with open(LOG_FILE, "w") as file:
    file.write("")

def terminate(pressed):
    return len(pressed) >= 3 and \
        pressed[-1] == pressed[-2] == pressed[-3] \
        == keyboard.Key.esc

def log(string):
    with open(LOG_FILE, "a") as file:
        file.write(string)

def press(key):
    pressed.append(key)
    
    if isinstance(key, keyboard.KeyCode):
        log(f"+{key.char}\n")
    else:
        log(f"+[{key.name.upper()}]\n")

def release(key):
    if isinstance(key, keyboard.KeyCode):
        log(f"-{key.char}\n")
    else:
        log(f"-[{key.name.upper()}]\n")

    if terminate(pressed):
        return False

print("Press [ESC] three times in succession to terminate recording.")
with keyboard.Listener(on_press = press, on_release = release) as listener:
    listener.join()

print("Quit.")
with open(LOG_FILE) as file:
    print(file.read())