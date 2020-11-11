# Week5 --- Task1---->Homework ----> Atabek
# 1)
'''Function that can read students marks and sorted who got the less than 3 or equal to 3.'''
# with open ('otsenki.txt', 'r') as file :

#     for line in file.readlines() :

#         if '1' in line :
#             print (line)
#         elif '2' in line :
#             print (line)    


# with open ('otsenki.txt', 'r') as f :
#     nums = [x for x in f.read().split()]
#     ball = []
#     for num in nums :
#         if num.isdigit():
#             ball.append(int(num))

#     res = int(sum(ball) / len(ball))

#     print(f'Средний балл класса : {res}')

# 2)
# file_name = input('Enter the name of your file: ')
# file_create = open(file_name,'w')
# while True:
#     file_things = input('Enter your file content, if you wanna close everything, just press the ENTER button!')
#     if file_things == '': break
#     file_create.write(file_things+'\n')
# file_create.close()

# 3)
# В текстовом файле посчитать количество строк, а также для каждой
# отдельной строки определить количество в ней символов и слов.

# with open('otsenki.txt') as file:
#     file = file.readlines()
#     len_count = len(file)
#     print(f'In file {len_count} string\n')
#     string_count = 0
#     iteration = 1
#     for string in file:
#         count = string.count(' ') + 1
#         len_string = len(string) - 1
#         print(f'V {iteration}oy stroke {len_string} simvola and {count} slova\n')
#         iteration += 1 


# 4)
# Создайте файл nums.txt, содержащий несколько чисел, записанных через пробел.
# Напишите программу, которая подсчитывает и выводит на экран общую сумму
# чисел, хранящихся в этом файле.

# with open('nums.txt', 'r') as file:
#     num1_line = 1
#     for line in file.readlines():
#         nums = list(map(int, line.split()))
#         print(f'Summa chisel {num1_line} stroki - {sum(nums)}')
#         num1_line += 1

# 5)
# Считать из файла input.txt 10 чисел (числа записаны через пробел). Затем
# записать их произведение в файл output.txt.

# from functools import reduce

# with open ('input.txt', 'r') as file :
#     line_num = 1
#     with open ('output.txt', 'w+') as f :
#         for line in file.readlines():
#             nums = list(map(int, line.split()))
#             res = reduce(lambda x, y: x * y, nums)
            
#             f.writelines('Произведение чисел '+ str(line_num) + ' строки - ' + str(res) + str('\n'))
#             line_num += 1

# 6)
# В файле записаны в целые числа. Найти максимальное и минимальное число и
# записать в другой файл.

# with open ('Task6_nums_input.txt', 'r') as file :
#     line_num = 1
#     with open ('Task6_nums_output.txt', 'w+') as f :
#         for line in file.readlines() :
#             nums = list(map(int, line.split()))
#             min_num = min(nums)
#             max_num = max(nums)
#             f.writelines('Stroka ' + str(line_num) + ' - ' + 'Minimum number is: '
#                         + str(min_num) + ', Maximum number is: ' + str(max_num) + str('\n'))
#             line_num += 1

# 7)
# В файле записаны в столбик целые числа. Отсортировать их по
# возрастанию суммы цифр и записать в другой файл.


# 8) Напишите программу которая будет записывать данные в
# файл, для примера данные филиалы офисов Google:
# 1) google_kazakstan.txt
# 2) google_paris.txt
# 3)google_uar.txt
# 4)google_kyrgystan.txt
# 5)google_san_francisco.txt
# 6)google_germany.txt
# 7)google_moscow.txt
# 8)google_sweden.txt
# Когда пользователь напишет “Hello”
# Ваша программа должна предоставить список филиалов.
# После этого программа должна записать жалобу от пользователя в тот файл который
# выбрал пользователь из списка.
# Подсказка использовать конструкцию with open
# hello = input('Welcome : ').lower()
# ------------------||||||||------||||||||||||
# if hello == 'hello' :
#     print('''1) google_kazakstan
# 2) google_paris
# 3) google_uar
# 4) google_kyrgystan
# 5) google_san_francisco
# 6) google_germany
# 7) google_moscow
# 8) google_sweden''')

#     country = int(input('Выберите страну (1-8) : '))
#     if country == 1:
#         with open('google_kazakstan.txt', 'a') as file:
#             complain = input('Enter your complains: ')
#             file.writelines(complain + '\n')
#             print('Thanks! We got your complainings!')
#     elif country == 2:
#         with open('google_patis.txt', 'a') as file:
#             complain = input('Enter your complains: ')
#             file.writelines(complain + '\n')
#             print('Thanks! We got your complainings!')
#     elif country == 3:
#         with open('google_uar.txt',  'a') as file:
#             complain = input('Enter your complains: ')
#             file.writelines(complain + '\n')
#             print('Thanks! We got your complaining!')
#     elif country == 4:
#         with open('google_kyrgyzstan.txt', 'a') as file:
#             complain = input('Enter your complains: ')
#             file.writelines(complain + '\n')
#             print('Thanks! We got your complaining!')
#     elif country == 5:
#         with open('google_san_francisco.txt', 'a') as file:
#             complain = input('Enter your complains: ')
#             file.writelines(complain + '\n')
#             print('Thanks! We got your complaining!')
#     elif country == 6:
#         with open('google_germany.txt', 'a') as file:
#             complain = input('Enter your complains: ')
#             file.writelines(complain + '\n')
#             print('Thanks! We got your complaining!')
#     elif country == 7:
#         with open('google_moscow.txt', 'a') as file:
#             complain = input('Enter your complains: ')
#             file.writelines(complain + '\n')
#             print('Thanks! We got your complaining!')
#     elif country == 8:
#         with open('google_sweden.txt', 'a') as file:
#             complain = input('Enter your complains: ')
#             file.writelines(complain + '\n')
#             print('Thanks! We got your complaining!')
#     else:
#         print('There is no country like this!!!')
# else:
#     print('Type "Hello"')

# 8)
# Распаковать json файл и получить значение у ключа “age”
# Ввод: '{ "name":"John", "age":30, "city":"New York"}'
# Вывод: 30

# import json
# with open('task1_8.json', 'r+') as f :
#     best = json.load(f)
#     print(best['age'])

# 9)
# Преобразовать словарь в json формат
# Ввод: {
# "name": "John",
# "age": 30,
# "city": "New York"
# }
# Вывод: '{"name":"John", "age":30, "city":"New York"}'
#----------|||||||--------||||||||||-----------|||||||||||

# import json
# to_json = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
# with open('task1_9.json', 'r+') as file:
#     json.dump(to_json, file)

























