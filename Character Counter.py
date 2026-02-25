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


    def find_max(numbers):
    return max(numbers)

def main():
    print("=== Maximum Finder ===")

    nums = []

    for i in range(3):
        num = int(input("Enter number: "))
        nums.append(num)

    print("Maximum number is:", find_max(nums))

if __name__ == "__main__":
    main()


    def generate_username(first, last):
    return first.lower() + "_" + last.lower()

def main():
    print("=== Username Generator ===")

    first = input("Enter first name: ")
    last = input("Enter last name: ")

    username = generate_username(first, last)

    print("Generated username:", username)

if __name__ == "__main__":
    main()


    def calculate_total(prices):
    return sum(prices)

def main():
    print("=== Shopping Calculator ===")

    prices = []

    for i in range(3):
        price = float(input("Enter price: "))
        prices.append(price)

    total = calculate_total(prices)

    print("Total price:", total)

if __name__ == "__main__":
    main()