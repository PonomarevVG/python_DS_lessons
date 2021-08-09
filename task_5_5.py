# Задание 5.5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

print('Вводите последовательно числа, которые будут записываться в файл task_5_5_file.txt .'
      'Ввод пустой строки будет означать окончание записи')
line = ''
with open('task_5_5_file.txt', 'w') as write_f:
    while True:
        s = input('Введите число для записи в файл: ')
        if s == '':
            break
        line += s + ' '
    if len(line) > 0:
        line = line[0:len(line)-1]
    print(line, file=write_f)

sum = 0.0
with open('task_5_5_file.txt') as read_f:
    values = read_f.readline().split(' ')

for value in values:
    sum += float(value)
print(f'Сумма чисел в файле = {sum}')
