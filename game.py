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