number1=int(input('a='))
number2=int(input('b='))
op = input()
result = None

if op =='+':
    result = number1 + number2
    print(a+b)
elif op =='-':
    result=number1-number2
    print(a-b)
elif op =='*':
    result=number1*number2
    print(a*b)
elif op =='/':
    result=number1/number2
    print(a/b)
else:
    print('я умею делать только: +, -, *, / !')



my_str= str(number1) +'+' + str(number2) + '=' + str(number1+number2)
print(my_str)
