def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    return False

def main():
    print("=== Email Validator ===")

    email = input("Enter email: ")

    if is_valid_email(email):
        print("Valid email")
    else:
        print("Invalid email")

if __name__ == "__main__":
    main()

def sum_of_digits(number):
    total = 0
    for digit in str(abs(number)):
        total += int(digit)
    return total

def main():
    num = int(input("Enter a number: "))
    print("Sum of digits:", sum_of_digits(num))

if __name__ == "__main__":
    main()    