numbers = []
for i in range(1,11):
    for i in input('Введите числа: ').split():
        numbers.append(int(i))
print(numbers)
print(sum(numbers))