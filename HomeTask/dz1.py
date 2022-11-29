#1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# num = int(input())
# if 5 < num < 8:
#     print('Weekend')
# elif 0 < num < 6:
#     print('Workday')
# else:
#     print("it's not a day of the week")


#2 Напишите программу для. проверки ложности утверждения (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((w and z) or not y or (not x == (not w))):
#                     print(x, y, z, w)


# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#     print(1)
# elif x < 0 < y:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# elif x > 0 > y: 
#     print(4)
# else:
#     print("Error, 0 entered")


#4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# n = input()
# match n:
#     case"1":
#         print("x > 0, y > 0")
#     case"2":
#         print("x < 0, y > 0")
#     case"3":
#         print("x < 0, y < 0")
#     case"4":
#         print("x > 0, y < 0")
#     case _:
#         print("error")


# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве

# x_1 = int(input())
# y_1 = int(input())
# x_2 = int(input())
# y_2 = int(input())

# print(f"{((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5:.3f}")

