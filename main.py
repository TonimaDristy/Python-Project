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