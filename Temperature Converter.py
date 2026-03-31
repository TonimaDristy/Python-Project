def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(lb):
    return lb / 2.20462

def main():
    print("=== Weight Converter ===")
    print("1. KG to Pounds")
    print("2. Pounds to KG")

    choice = input("Enter choice: ")

    if choice == "1":
        kg = float(input("Enter kg: "))
        print("Pounds:", kg_to_pounds(kg))

    elif choice == "2":
        lb = float(input("Enter pounds: "))
        print("KG:", pounds_to_kg(lb))

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()