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