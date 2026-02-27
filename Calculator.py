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