def print_table(number):
    print(f"\nMultiplication Table of {number}")
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

def main():
    print("=== Table Generator ===")

    num = int(input("Enter a number: "))
    print_table(num)

if __name__ == "__main__":
    main()