# Написать программу, которая считывает список слов и находит слова, содержащие более трех гласных букв.
with open('words.txt', 'r') as f:
    words = f.read().split()

vowels = 'aeiouyAEIOUY'

for word in words:
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    if count > 3:
        print(word)

