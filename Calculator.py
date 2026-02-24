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