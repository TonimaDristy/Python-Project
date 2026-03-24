import random

colors = ["Red", "Blue", "Green", "Yellow", "Purple"]

while True:
    input("Press Enter to pick a random color...")
    
    print("Color:", random.choice(colors))

    again = input("Pick again? (y/n): ")
    if again.lower() != "y":
        break