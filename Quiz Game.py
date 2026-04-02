def ask_questions():
    questions = [
        ("Capital of Germany?", "berlin"),
        ("5 * 6 = ?", "30"),
        ("Color of the sky?", "blue")
    ]

    score = 0

    for q, ans in questions:
        user = input(q + " ").strip().lower()
        if user == ans:
            print("Correct!")
            score += 1
        else:
            print("Wrong! Correct answer:", ans)

    return score


def main():
    print("=== Multi Question Quiz ===")
    score = ask_questions()
    print(f"Final Score: {score}/3")


if __name__ == "__main__":
    main()