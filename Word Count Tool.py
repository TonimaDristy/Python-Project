text = input("Enter a sentence or paragraph: ")

words = text.split()
word_count = len(words)
char_count = len(text)
line_count = text.count("\n") + 1

print("Word Count:", word_count)
print("Character Count:", char_count)
print("Line Count:", line_count)