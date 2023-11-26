# Написать программу, которая удаляет из списка все дубликаты.
numbers = [1, 2, 3, 4, 5, 5, 6, 6, 7, 7, "a", "b", "c", "d", "a", "b", "c", "d", "a", 'aaa', 'bbb', 'ccc', 'ddd', 'eee', 'ddd', 'eee']

unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)