def write_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

def main():
    print("=== File Writer ===")

    filename = input("Enter filename: ")
    content = input("Enter content: ")

    write_file(filename, content)

    print("File saved successfully.")

if __name__ == "__main__":
    main()
    def main():
    num = int(input("Enter a number: "))

    if num % 5 == 0:
        print("It is a multiple of 5")
    else:
        print("Not a multiple of 5")

if __name__ == "__main__":
    main()

    def main():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    area = length * width

    print("Area of rectangle:", area)

if __name__ == "__main__":
    main()
    def main():
    char = input("Enter a character: ")

    if char.isalpha():
        print("It is an alphabet")
    else:
        print("It is not an alphabet")

if __name__ == "__main__":
    main()