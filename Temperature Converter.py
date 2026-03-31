def meters_to_km(m):
    return m / 1000

def km_to_meters(km):
    return km * 1000

def main():
    print("=== Length Converter ===")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")

    choice = input("Enter choice: ")

    if choice == "1":
        m = float(input("Enter meters: "))
        print("Kilometers:", meters_to_km(m))

    elif choice == "2":
        km = float(input("Enter kilometers: "))
        print("Meters:", km_to_meters(km))

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()