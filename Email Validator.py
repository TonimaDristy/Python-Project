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