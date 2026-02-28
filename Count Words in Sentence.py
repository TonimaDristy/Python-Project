def count_words(sentence):
    words = sentence.split()
    return len(words)

def main():
    print("=== Word Counter ===")

    sentence = input("Enter a sentence: ")
    total = count_words(sentence)

    print("Total words:", total)

if __name__ == "__main__":
    main()

    def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if a > b:
        print("Largest number is:", a)
    elif b > a:
        print("Largest number is:", b)
    else:
        print("Both numbers are equal")

if __name__ == "__main__":
    main()
    def main():
    minutes = int(input("Enter total minutes: "))

    hours = minutes // 60
    remaining_minutes = minutes % 60

    print("Hours:", hours)
    print("Remaining Minutes:", remaining_minutes)

if __name__ == "__main__":
    main()

    def main():
    char = input("Enter a character: ").lower()

    if char in "aeiou":
        print("It is a vowel")
    else:
        print("It is a consonant")

if __name__ == "__main__":
    main()