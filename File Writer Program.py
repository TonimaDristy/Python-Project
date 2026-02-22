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