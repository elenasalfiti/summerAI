#task 3
word = input("Insert a word: ")
def count_letters(word):
    return len([x for x in word if x.isalpha()])

print("The word has", count_letters(word), "letters")