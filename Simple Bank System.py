balance = 0

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount

def show_balance():
    print("Current balance:", balance)

def main():
    while True:
        print("\n=== Bank System ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount: "))
            withdraw(amount)

        elif choice == "3":
            show_balance()

        elif choice == "4":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()