def ask_question():
    print("Which country is known as the Land of the Rising Sun?")
    answer = input("Enter answer: ")

    if answer.lower() == "japan":
        return True
    return False

def main():
    print("=== Country Quiz ===")

    score = 0

    if ask_question():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    print("Your score:", score)

if __name__ == "__main__":
    main()