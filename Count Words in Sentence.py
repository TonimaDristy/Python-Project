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