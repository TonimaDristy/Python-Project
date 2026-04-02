def ask_question():
    print("Is Python a programming language? (yes/no)")
    answer = input("Enter answer: ")

    if answer.lower() == "yes":
        return True
    return False

def main():
    print("=== Yes/No Quiz ===")

    score = 0

    if ask_question():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    print("Your score:", score)

if __name__ == "__main__":
    main()