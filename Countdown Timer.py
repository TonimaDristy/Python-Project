import time

def countdown(seconds):
    while seconds > 0:
        print("Time left:", seconds, "seconds")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

def main():
    print("=== Countdown Timer ===")

    seconds = int(input("Enter seconds: "))
    countdown(seconds)

if __name__ == "__main__":
    main()

    def calculate_age(current_year, birth_year):
    return current_year - birth_year

def main():
    print("=== Age Calculator ===")

    current_year = int(input("Enter current year: "))
    birth_year = int(input("Enter your birth year: "))

    age = calculate_age(current_year, birth_year)

    print("Your age is:", age)

if __name__ == "__main__":
    main()

    def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

def main():
    print("=== Vowel Counter ===")

    text = input("Enter text: ")

    total = count_vowels(text)

    print("Number of vowels:", total)

if __name__ == "__main__":
    main()