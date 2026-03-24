import random

while True:
    number = random.randint(1, 10)
    
    guess = int(input("Guess a number (1-10): "))
    
    if guess == number:
        print("Correct!")
    else:
        print("Wrong! The number was:", number)

    again = input("Play again? (y/n): ")
    if again.lower() != "y":
        break