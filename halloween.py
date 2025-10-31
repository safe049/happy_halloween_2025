import os
import time

def orange_text(text):
    return f"\033[38;5;208m{text}\033[0m"

def clear():
    os.system("clear")

def sleep_clear(sec):
    time.sleep(sec)
    clear()

def main():
    while True:
        clear()
        print("🎃")

        sleep_clear(1.5)
        print("HAPPY")

        sleep_clear(1.5)
        print(orange_text("HALLOWEEN"))

        sleep_clear(1.5)

if __name__ == "__main__":
    main()
