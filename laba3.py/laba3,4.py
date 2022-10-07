n = int(input('Введите любое натуральное число: '))
print('ВОТ ВАША ПИРАМИДА: ')
for i in range(1,n+1):
    for a in range(1, n+1-i):
        print('', end=' ')
    for b in range (1,i+1):
        print(b, end= '')
    for c in range(i-1,0,-1):
        print(c, end = '')
    print()
