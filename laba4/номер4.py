slovarb = {1: 'Что такое функция?', 2: 'Определение предела.', 3: 'Спой песню маи.', 4: 'Тебе повезло!!!Зачёт'}
key = int(input('Введите номер билета от 1 до 4, чтобы получить задания: '))
def get_value(dictionary):
    value = dictionary.get(key)
    print(value)
get_value(slovarb)