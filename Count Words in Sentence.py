def count_words(sentence):
    words = sentence.split()
    return len(words)

def main():
    print("=== Word Counter ===")

    sentence = input("Enter a sentence: ")
    total = count_words(sentence)

    print("Total words:", total)

if __name__ == "__main__":
    main()