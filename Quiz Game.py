import time

def ask_question():
    print("You have 5 seconds!")
    start = time.time()

    answer = input("What is 10 + 5? ")

    end = time.time()

    if end - start > 5:
        print("Time's up!")
        return False

    return answer == "15"


def main():
    print("=== Timed Quiz ===")

    if ask_question():
        print("Correct!")
    else:
        print("Wrong!")


if __name__ == "__main__":
    main()