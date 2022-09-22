def line(x):
    global argument1
    argument1= 3+2
    y = 2 + 3 * x 
    return y 


argument2 = int(input('введите x\n'))

print(line(argument2))
print(argument1)
