# Написать программу, которая удаляет из списка все элементы, стоящие на четных позициях.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
even_values = [i for i in my_list if i %2 != 0]
print(even_values)

