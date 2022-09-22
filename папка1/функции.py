month = input('какой месяц?\n')
year = int(input('Какой у нас год?\n'))
if month =='январь' or month =='Март' or month== 'Май' :
    print(31)
elif month =='февраль' and (year % 4 == 0 and year % 100 !=0 or year % 400 == 0):
    print(29) 
elif month == 'февраль' and not (year % 4==0 and year % 100!=0 or year % 400 ==0):
    print(28)
else :
    print(30)