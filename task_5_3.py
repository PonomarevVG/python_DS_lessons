# Задание 5.3
# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

averange_salary = 0.0
lines_count = 0
print('Список сотрудников с окладами < 20 000 руб.')
with open('task_5_3_file.txt') as read_f:
    for s in read_f:
        if s[len(s)-1] == '\n':
            s = s[0:len(s)-1]
        words = s.split(' ')
        surname = words[0]
        salary = float(words[1])
        averange_salary += salary
        lines_count += 1
        if salary < 20000.0:
            print(f'Фамилия: "{surname}", оклад {salary} руб.')
        lines_count += 1
print(f'Средний оклад = {averange_salary / lines_count}')