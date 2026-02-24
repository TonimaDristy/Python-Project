def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def main():
    print("=== Prime Number Checker ===")

    num = int(input("Enter number: "))

    if is_prime(num):
        print("It is prime")
    else:
        print("Not prime")

if __name__ == "__main__":
    main()