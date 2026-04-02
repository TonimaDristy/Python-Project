def ask_question():
    print("What gas do plants absorb from the atmosphere?")
    answer = input("Enter answer: ")

    if answer.lower() == "carbon dioxide":
        return True
    return False

def main():
    print("=== Science Quiz ===")

    score = 0

    if ask_question():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    print("Your score:", score)

if __name__ == "__main__":
    main()