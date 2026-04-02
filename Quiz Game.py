def ask_question():
    print("What does CPU stand for?")
    answer = input("Enter answer: ")

    if answer.lower() == "central processing unit":
        return True
    return False

def main():
    print("=== Computer Quiz ===")

    score = 0

    if ask_question():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    print("Your score:", score)

if __name__ == "__main__":
    main()