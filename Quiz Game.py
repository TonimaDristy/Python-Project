def ask_question():
    correct_answer = "python"
    attempts = 3

    while attempts > 0:
        answer = input("Which language are you coding in? ").lower()

        if answer == correct_answer:
            return True

        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")

    return False


def main():
    print("=== Attempt Based Quiz ===")

    if ask_question():
        print("Correct!")
    else:
        print("Out of attempts!")


if __name__ == "__main__":
    main()