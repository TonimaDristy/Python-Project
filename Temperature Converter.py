def calculate_si(p, r, t):
    return (p * r * t) / 100

def main():
    print("=== Simple Interest Calculator ===")

    p = float(input("Enter principal: "))
    r = float(input("Enter rate (%): "))
    t = float(input("Enter time (years): "))

    print("Simple Interest:", calculate_si(p, r, t))

if __name__ == "__main__":
    main()