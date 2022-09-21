#ЗАДАНИЕ ОДИН
#1. a and b
#2. (a and b) or b
#3. (a and b) or not (a and b)
#4. a and b or not (a or b) or b
#5. b and b or not a and (a or b or a) or not (a or b)
#6. 1 << 2
#7. 1 & 0 | 1 >> 1
#8. 1 & 0 | 1 >> 0
#9. 0b101 & 0b111 ^ 0b111 | 0b010

#1
v='#1.'
a= True
b= False
print(v,a and b)


#2
v='#2.'
a= True
b= False
print(v,(a and b) or b)

#3
v='#3.'
a= True
b= False
print(v,(a and b) or not(a and b))

#4
v='#4.'
a= True
b= False
print(v,a and b or not (a or b) or b)

#5
v='#5.'
a= True
b= False
print(v,b and b or not a and (a or b or a) or not (a or b))

#6
v='#6.'
print(v,1<<2)

#7
v='#7.'
print(v,1 & 0 | 1 >> 1)

#8
v='#8.'
print(v,1 & 0 | 1 >> 0)

#9
v='#9.'
print(v, 0b101 & 0b111 ^ 0b111 | 0b010)


#ЗАДАНИЕ 2
a=int(input('введите число a: '))
b=int(input('введите число b: '))
if a<b :
    print (a)
else:
    print(b)

#ЗАДАНИЕ 3
a = int(input('Введите первое число : '))
b = int(input('Введите второе число : '))
с = int(input('Введите третье число : '))

print('Максимальное число:',max(a,b,с))

#ЗАДАНИЕ 4. Напишите программу, которая принимает с клавиатуры 3 числа и 
# выводит на экран количество уникальных чисел.
a = int(input('Введите первое число : '))
b = int(input('Введите второе число : '))
c= int(input('Введите третье число : '))
if a==b & a==c:
    print('Уникальных чисел: ', 1)
elif a!=b & a!=c & b!=c:
    print('Уникальных чисел: ',3)
else:
    print('Уникальных чисел: ',2)


