#print("hello world")

# int = целые числа, float = числа с плавающей точкой, boolean? str, list, None
# \n new string
# value = None
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12345
# print(type(value))
#s = "hello \nwordsss"
#print(s)  # вывод строки
#print(a, '-', b, '-', s)
#print('{1} - {2} - {0}'.format(a, b, s))
#print(f'{a} - {b} - {s}')  # интерполяция
#f=True/False
#print(f)

#list = ['1','2','3','hello']
#print(list)


#print('Enter a: ')
#a = int(input())  #float если дробные
#print('Enter b: ')
#b = int(input())   #float если дробные
#print(a,'+', b, '=', a+b)
#print(f'{a} {b}')


# Арифмитические операции +, -, *, /, %, //, **
# ** возведение в степень, / деление, % деление с остатком
# 
#a = 12.2333
#b = 3
#c= round(a*b, 4)  # цифра после запятой
#print(c)

#a = 2
#a +=5  # * или другие
#print(a)

#a = int(input('a = '))
#b = int(input('b = '))
#if a > b:
    #print(a)
#else:
    #print(b)

# Цикл WHILE
#original = 23
#inverted = 0
#while original !=0:
    #inverted = inverted * 10 + (original % 10)
    #original //=10
#else:
    #print('qwerr')
    #print('stop')
#print(inverted)

# Цикл FOR
#for i in 'qwerty':
    #print(i)


# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...