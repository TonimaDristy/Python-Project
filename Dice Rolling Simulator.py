import random

jokes = [
    "Why did the computer crash? It had a bad driver.",
    "Why do programmers prefer dark mode? Less light, fewer bugs.",
    "Why did Python go to school? To improve its class."
]

while True:
    input("Press Enter to get a joke...")
    
    print(random.choice(jokes))

    again = input("Another joke? (y/n): ")
    if again.lower() != "y":
        break