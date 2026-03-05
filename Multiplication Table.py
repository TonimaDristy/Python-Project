def print_table(number):
    print(f"\nMultiplication Table of {number}")
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

def main():
    print("=== Table Generator ===")

    num = int(input("Enter a number: "))
    print_table(num)

if __name__ == "__main__":
    main()

    def main():
    text = input("Enter text: ")

    words = len(text.split())
    characters = len(text)

    print("Total words:", words)
    print("Total characters:", characters)

if __name__ == "__main__":
    main()