import random

def generate_number():
    return random.randint(1, 10)

def check_guess(secret, guess):
    if guess == secret:
        return True
    return False

def main():
    print("=== Number Guessing Game ===")

    secret_number = generate_number()

    guess = int(input("Guess a number between 1 and 10: "))

    if check_guess(secret_number, guess):
        print("Correct! You win!")
    else:
        print("Wrong! The number was:", secret_number)

if __name__ == "__main__":
    main()

    import math

def main():
    num = int(input("Enter a number: "))

    root = math.isqrt(num)

    if root * root == num:
        print("It is a perfect square")
   def main():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    unique_numbers = list(set(numbers))

    print("After removing duplicates:", unique_numbers)

if __name__ == "__main__":
    main()