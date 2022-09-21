name = input('Как вас зовут?')
age = input('Сколько лет?')
if name == '' and age=='':
    print('безымяный? ты чё педик старый?')
elif age == '':
    print('ты чё педик старый')
elif name == '':
    print ('вы безымяный?')
else:
    print('спасибо')