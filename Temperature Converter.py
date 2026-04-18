def main():
    list1 = list(map(int, input("Enter first list: ").split()))
    list2 = list(map(int, input("Enter second list: ").split()))

    common = list(set(list1) & set(list2))

    print("Common elements:", common)

if __name__ == "__main__":
    main()