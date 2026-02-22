def get_user_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    return name, age, city

def display_user_info(name, age, city):
    print("\n=== User Information ===")
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

def main():
    print("=== User Info System ===")

    name, age, city = get_user_info()
    display_user_info(name, age, city)

if __name__ == "__main__":
    main()