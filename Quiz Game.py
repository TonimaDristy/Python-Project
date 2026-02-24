def ask_question():
    print("What is the capital of France?")
    answer = input("Enter answer: ")

    if answer.lower() == "paris":
        return True
    return False

def main():
    print("=== Quiz Game ===")

    score = 0

    if ask_question():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    print("Your score:", score)

if __name__ == "__main__":
    main()