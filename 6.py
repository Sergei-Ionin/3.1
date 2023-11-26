# Написать программу, которая запрашивает у пользователя строку и выводит на экран все ее подстроки длиной не менее трех символов.
user_input = input("Введите строку: ")

for i in range(len(user_input)-2):
    if (len(user_input[i:i+3]) >= 3):
        print(user_input[i:i+3])

# Thank you very much for using this program!