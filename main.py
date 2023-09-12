# завдання 1

# a = float(input("Сторона a: "))
# b = float(input("Сторона b: "))
#
# s = a * b
# p = 2 * (a + b)
#
# print("S:", s, "P:", p)

# завдання 2

# import math
#
# a = float(input("Число a: "))
# b = float(input("Число b: "))
#
# x = math.sqrt(a * b)
#
# print(f"Середнє геометричне: {x}")

# завдання 3
#
# x1 = float(input("x1: "))
# y1 = float(input("y1: "))
# x2 = float(input("x2: "))
# y2 = float(input("y2: "))
#
# a = abs(x2 - x1)
# b = abs(y2 - y1)
#
# s = (a * b)
# p = 2 * (a + b)
#
# print(f"S: {s}", f"P: {p}")

# завдання 4

# a = int(input("Ціле число a: "))
#
# if a / 2 == int(a / 2):
#     print(f"{a} - число парне.")
# else:
#     print(f"{a} - число непарне.")

# завдання 5

# a = int(input("Ціле число a: "))
# b = int(input("Ціле число b: "))
# c = int(input("Ціле число c: "))
#
# if a < b < c :
#  print("Висловлення a<b<c - правильне")
# else:
#  print("Висловлення a<b<c - неправильне")
#
# if a > 0 or b > 0 or c > 0:
#     print("Висловлення (Хоча б одне з чисел додатне) - правильне.")
# else:
#     print("Висловлення (Хоча б одне з чисел додатне) - неправильне.")
#
# positive_n = 0
# if a > 0:
#     positive_n += 1
# if b > 0:
#     positive_n += 1
# if c > 0:
#     positive_n += 1
# if positive_n == 1:
#     print("Bисловлення (Рівно одне число додатнє) - правильне.")
# else:
#     print("Bисловлення (Рівно одне число додатнє) - неправильне.")

# завдання 6

# x = int(input("x (ціле число в діапазоні 1-8): "))
# y = int(input("y (ціле число в діапазоні 1-8): "))
#
# if 1 <= x <= 8 and 1 <= y <= 8:
#
#  if (x + y) % 2 == 0:
#     print(f"Поле з координатами ({x}, {y}) є білим - неправильне твердження.")
#  else:
#     print(f"Поле з координатами ({x}, {y}) є білим - правильне твердження.")
# else:
#  print("Введіть числа в діапазоні 1-8.")

# завдання 7

# x1 = int(input("x1 (ціле число в діапазоні 1-8): "))
# y1 = int(input("y1 (ціле число в діапазоні 1-8): "))
# x2 = int(input("x2 (ціле число в діапазоні 1-8): "))
# y2 = int(input("y2 (ціле число в діапазоні 1-8): "))
#
# if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
#  if(x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 -y1)):
#   print(f"Ферзь за один хід може перейти з поля ({x1},{y1}) на поле ({x2},{y2})")
#  else:
#   print(f"Ферзь за один хід не може перейти з поля ({x1},{y1}) на поле ({x2},{y2})")
# else:
#  print("Введіть числа в діапазоні 1-8.")

# завдання 8

# A = int(input("Ціле число A: "))
# B = int(input("Ціле число B (A<B): "))
#
# if A < B:
#  interval_n = 0
#  print("Всі цілі числа між А та В включно: ")
#  for number in range(A, B + 1):
#         print(number)
#         interval_n += 1
#  print("Кількість N всіх цілих чисел між A та B (включно):", interval_n)
# else:
#  print("Цілі числа А та В мають задовольняти умову А<B.")

# завдання 9

# N = int(input("Ціле число N (N>0): "))
#
# reversed_n = 0
# while N > 0:
#     last_n = N % 10
#     reversed_n = reversed_n * 10 + last_n
#     N //= 10
# print("Число, що отримане при читанні числа N справа наліво: ", reversed_n )
# if N < 0:
#     print("Число N має бути більше 0.")

# завдання 10
#
# massif = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# average = sum(massif) / len(massif)
#
# for i in range(len(massif)):
#     if massif[i] > average:
#         massif[i] -= 18
#
# print("Масив після редагування відповідно до умови:", massif)

# завдання 11

# N = int(input("Ціле число N (N>1): "))
# def number(N):
#     if N <= 1:
#         return False
#     elif N == 2:
#         return True
#     elif N % 2 == 0:
#         return False
#
#     highest_divider = int(N**0.5) + 1
#     for divisor in range(3, highest_divider, 2):
#         if N % divisor == 0:
#             return False
#     return True
# print(number(N))

# завдання 12

# import math
#
# x = 2
# y = 10.35
# z = 2.379
#
# siny = math.sin(y)
#
# a = x + (z ** 2) / (3 + z * siny)
#
# print(f"Значення функції {a}:")

# завдання 13

# name = input("Ім'я: ")
# surname = input("Прізвище: ")
# phone_n = input("Номер телефону: ")
#
# if name and surname and phone_n:
#         print("Спасибі")
# else:
#         print("Не залишайте жодні поля порожніми")



# name = input("Ім'я: ")
# surname = input("Прізвище: ")
# phone_n = input("Номер телефону: ")
#
# if name or surname or phone_n:
#         print("Спасибі")
# else:
#     print("Не залишайте всі поля порожніми.")



# name = input("Ім'я: ")
# surname = input("Прізвище: ")
# phone_n = input("Номер телефону: ")
#
# if name and surname and phone_n:
#         print("Спасибі")
# elif name and surname:
#         print("Спасибі")
# else:
#         print("Обов'язково вкажіть ім'я та прізвище.")

# завдання 14

# for counter in range(5):
#     number = input("Введіть число (5 спроб): ")
#     if number == "5":
#         print("Молодець!")
#         break
# else:
#     print("Ви не вгадали.")

# завдання 15

# start = 0
# end = 100
# step = 1
#
# for number in range(start, end, step):
#  if number % 13 == 0:
#      print(number)

# завдання 16

# first_line = input("Перший рядок: ")
# second_line = input("Другий рядок: ")
#
# unite_line = first_line + second_line
# print(unite_line)
#
# multiply_line = first_line * 10
# print(multiply_line)
#
# add_simbol = input("Який символ треба вставити?")
# place = int(input(f"Номер символа перед яким треба вставити {add_simbol}: "))
# combine_line = first_line[:place] + add_simbol + first_line[place:]
# print(combine_line)






























