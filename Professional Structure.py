def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a + b)

def greet():
    name = input("Enter name: ")
    print("Hello,", name)

def show_menu():
    print("\n=== MENU ===")
    print("1. Greet")
    print("2. Add Numbers")
    print("3. Exit")

def main():
    while True:
        show_menu()

        choice = input("Enter choice: ")

        if choice == "1":
            greet()
        elif choice == "2":
            add()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()