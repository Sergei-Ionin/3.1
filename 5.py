# Написать программу, которая считывает данные из CSV-файла и создает словарь, где ключами являются значения в столбце «Name», а значениями — соответствующие им словари с информацией о поле, возрасте и зарплате.
import csv

data = {}
with open('output.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
            name = row['Name']
            data[name] = {
                    'gender': row['Gender'],
                        'age': int(row['Age']),
                            'salary': int(row['Salary'])
}

print(data)