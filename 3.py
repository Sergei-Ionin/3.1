# Написать программу, которая находит второй по величине элемент в списке.
def second_largest(numbers):
    numbers.sort()
    if len(numbers) < 2:
        return None
    return numbers[-2]

numbers = [5, 3, 1, 8, 6, 4, 7]
print(second_largest(numbers))