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