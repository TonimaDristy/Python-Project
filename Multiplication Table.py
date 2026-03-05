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
    def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True

def main():
    num = int(input("Enter number: "))

    if is_prime(num):
        print("Prime number")
    else:
        print("Not prime")

if __name__ == "__main__":
    main()
    def main():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    unique_numbers = list(set(numbers))
    unique_numbers.sort()

    if len(unique_numbers) >= 2:
        print("Second largest:", unique_numbers[-2])
    else:
        print("Not enough numbers")

if __name__ == "__main__":
    main()
    def main():
    usd = float(input("Enter amount in USD: "))
    rate = 110  # example rate

    bdt = usd * rate

    print("Amount in BDT:", bdt)

if __name__ == "__main__":
    main()