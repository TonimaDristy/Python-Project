import time

def countdown(seconds):
    while seconds > 0:
        print("Time left:", seconds, "seconds")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

def main():
    print("=== Countdown Timer ===")

    seconds = int(input("Enter seconds: "))
    countdown(seconds)

if __name__ == "__main__":
    main()