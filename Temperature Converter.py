def circle_perimeter(r):
    return 2 * 3.1416 * r

def rectangle_perimeter(l, w):
    return 2 * (l + w)

def main():
    print("=== Perimeter Calculator ===")
    print("1. Circle")
    print("2. Rectangle")

    choice = input("Enter choice: ")

    if choice == "1":
        r = float(input("Enter radius: "))
        print("Perimeter:", circle_perimeter(r))

    elif choice == "2":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print("Perimeter:", rectangle_perimeter(l, w))

    else:
        print("Invalid choice")

main()