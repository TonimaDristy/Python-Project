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

    def main():
    text = input("Enter text: ").lower()
    vowels = "aeiou"
    count = 0

    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1

    print("Number of consonants:", count)

if __name__ == "__main__":
    main()

    def main():
    base = float(input("Enter base: "))
    exponent = float(input("Enter exponent: "))

    result = base ** exponent

    print("Result:", result)

if __name__ == "__main__":
    main()

    def main():
    num = input("Enter a number: ")

    reversed_num = num[::-1]

    print("Reversed number:", reversed_num)

if __name__ == "__main__":
    main()

    def main():
    num = int(input("Enter a number: "))

    if num % 3 == 0 and num % 7 == 0:
        print("Divisible by both 3 and 7")
    else:
        print("Not divisible by both")

if __name__ == "__main__":
    main()
    def main():
    principal = float(input("Enter principal: "))
    rate = float(input("Enter rate (%): "))
    time = float(input("Enter time (years): "))

    interest = (principal * rate * time) / 100
    total_amount = principal + interest

    print("Total amount:", total_amount)

if __name__ == "__main__":
    main()
    def main():
    text = input("Enter text: ")
    count = 0

    for char in text:
        if char.isupper():
            count += 1

    print("Uppercase letters:", count)

if __name__ == "__main__":
    main()