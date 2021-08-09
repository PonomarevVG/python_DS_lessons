# Задание 5.2
# Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open('task_5_2_file.txt') as read_f:
    lines = read_f.readlines()
    print(f'В файл task_5_2_file.txt число строк = {len(lines)} ')
    i = 1
    for s in lines:
        if i != len(lines):
            s = s[0:len(s) - 1]
        print(f'{i}: В строке: "{s}" число слов = {len(s.split(" "))}')
        i += 1