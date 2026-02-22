def check_strength(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) < 10:
        return "Medium"
    else:
        return "Strong"

def main():
    print("=== Password Strength Checker ===")

    password = input("Enter password: ")
    strength = check_strength(password)

    print("Password strength:", strength)

if __name__ == "__main__":
    main()