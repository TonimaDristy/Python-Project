def login(username, password):
    correct_username = "admin"
    correct_password = "1234"

    if username == correct_username and password == correct_password:
        return True
    return False

def main():
    print("=== Login System ===")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if login(username, password):
        print("Login successful")
    else:
        print("Login failed")

if __name__ == "__main__":
    main()