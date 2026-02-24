def count_characters(text):
    return len(text)

def main():
    print("=== Character Counter ===")

    text = input("Enter text: ")
    total = count_characters(text)

    print("Total characters:", total)

if __name__ == "__main__":
    main()