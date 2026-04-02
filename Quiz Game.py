def ask_questions():
    questions = {
        "2 + 2": "4",
        "3 + 5": "8",
        "10 - 4": "6"
    }

    score = 0

    for q, ans in questions.items():
        user = input(q + " = ")
        if user == ans:
            score += 1

    return score, len(questions)


def main():
    print("=== Graded Quiz ===")

    score, total = ask_questions()
    percent = (score / total) * 100

    print(f"Score: {score}/{total} ({percent:.2f}%)")

    if percent >= 80:
        print("Grade: A")
    elif percent >= 50:
        print("Grade: B")
    else:
        print("Grade: C")


if __name__ == "__main__":
    main()