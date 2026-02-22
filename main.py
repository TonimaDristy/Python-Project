# Function to greet user
def greet(name):
    print("Hello,", name + "!")
    print("Welcome to your Python project.")

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Main function
def main():
    print("=== Python Project Started ===")

 # Take user input
    name = input("Enter your name: ")
    greet(name)   


  # Take number input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    result = add_numbers(num1, num2)
    print("Sum is:", result)

    print("=== Program Finished ===")   

  # Run main function
if __name__ == "__main__":
    main()  

 def calculate_grade(marks):
    if marks >= 80:
        return "A+"
    elif marks >= 70:
        return "A"
    elif marks >= 60:
        return "A-"
    elif marks >= 50:
        return "B"
    else:
        return "Fail"

def main():
    print("=== Grade Calculator ===")

    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    grade = calculate_grade(marks)

    print("Student:", name)
    print("Grade:", grade)

if __name__ == "__main__":
    main()   



    def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    print("=== Even or Odd Checker ===")

    num = int(input("Enter a number: "))
    result = check_even_odd(num)

    print("The number is:", result)

if __name__ == "__main__":
    main()


def check_password(password):
    if password == "python123":
        return True
    else:
        return False

def main():
    print("=== Login System ===")

    password = input("Enter password: ")

    if check_password(password):
        print("Login successful")
    else:
        print("Wrong password")

if __name__ == "__main__":
    main()


 def add_item(item_list, item):
    item_list.append(item)

def show_items(item_list):
    print("Your items:")
    for item in item_list:
        print("-", item)

def main():
    print("=== List Manager ===")

    items = []

    for i in range(3):
        item = input("Enter item: ")
        add_item(items, item)

    show_items(items)

if __name__ == "__main__":
    main()       