import math

def circle_area(r):
    return math.pi * r * r

def rectangle_area(l, w):
    return l * w

def main():
    print("=== Area Calculator ===")
    print("1. Circle")
    print("2. Rectangle")

    choice = input("Enter choice: ")

    if choice == "1":
        r = float(input("Enter radius: "))
        print("Area:", circle_area(r))

    elif choice == "2":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print("Area:", rectangle_area(l, w))

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()