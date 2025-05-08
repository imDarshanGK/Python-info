phrase = input("Enter a phrase: ")
index = int(input("Enter the index of the word to display (starting from 0): "))

words = phrase.split(" ")

if 0 <= index < len(words):
    print(f"The word at index {index} is: {words[index]}")
else:
    print("Index out of range.")
