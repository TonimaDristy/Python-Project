import random

while True:
    input("Press Enter to toss a coin...")
    
    result = random.choice(["Heads", "Tails"])
    print("Result:", result)

    again = input("Toss again? (y/n): ")
    if again.lower() != "y":
        break