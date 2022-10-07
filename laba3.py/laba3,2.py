numbers = []
for i in range(1,11):
    for i in input('Введите числа: ').split():
        numbers.append(int(i))
        num_of_0 = numbers.count(0)
print(num_of_0)