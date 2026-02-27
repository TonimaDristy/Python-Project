def calculate_interest(principal, rate, time):
    return (principal * rate * time) / 100

def main():
    print("=== Simple Interest Calculator ===")

    principal = float(input("Enter principal: "))
    rate = float(input("Enter rate (%): "))
    time = float(input("Enter time (years): "))

    interest = calculate_interest(principal, rate, time)

    print("Simple Interest:", interest)

if __name__ == "__main__":
    main()

    def calculate_bmi(weight, height):
    return weight / (height * height)

def main():
    print("=== BMI Calculator ===")

    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (meters): "))

    bmi = calculate_bmi(weight, height)

    print("Your BMI is:", round(bmi, 2))

if __name__ == "__main__":
    main()

    def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def main():
    print("=== Leap Year Checker ===")

    year = int(input("Enter year: "))

    if is_leap_year(year):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

if __name__ == "__main__":
    main()

    def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"

def main():
    print("=== Calculator ===")

    while True:
        a = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        result = calculate(a, b, operator)
        print("Result:", result)

        again = input("Do you want to continue? (yes/no): ")
        if again.lower() != "yes":
            break

if __name__ == "__main__":
    main()


    def is_armstrong(number):
    num_str = str(number)
    power = len(num_str)
    total = 0

    for digit in num_str:
        total += int(digit) ** power

    return total == number

def main():
    print("=== Armstrong Number Checker ===")

    num = int(input("Enter number: "))

    if is_armstrong(num):
        print("It is an Armstrong number")
    else:
        print("Not an Armstrong number")

if __name__ == "__main__":
    main()

    def add_expense(expenses, amount):
    expenses.append(amount)

def show_total(expenses):
    print("Total expenses:", sum(expenses))

def main():
    expenses = []

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. Show Total")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, amount)

        elif choice == "2":
            show_total(expenses)

        elif choice == "3":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

    def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def main():
    num = int(input("Enter a number: "))
    print("The number is:", check_number(num))

if __name__ == "__main__":
    main()

    def greet(hour):
    if hour < 12:
        return "Good Morning"
    elif hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"

def main():
    hour = int(input("Enter current hour (0-23): "))
    print(greet(hour))

if __name__ == "__main__":
    main()