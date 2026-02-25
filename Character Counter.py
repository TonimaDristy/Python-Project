def count_characters(text):
    return len(text)

def main():
    print("=== Character Counter ===")

    text = input("Enter text: ")
    total = count_characters(text)

    print("Total characters:", total)

if __name__ == "__main__":
    main()


    def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

def main():
    print("=== Palindrome Checker ===")

    word = input("Enter a word: ")

    if is_palindrome(word):
        print("It is a palindrome")
    else:
        print("Not a palindrome")

if __name__ == "__main__":
    main()

    def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    print("=== Factorial Calculator ===")

    num = int(input("Enter a number: "))
    print("Factorial:", factorial(num))

if __name__ == "__main__":
    main()