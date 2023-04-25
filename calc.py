def Calculeit(number1, number2, oper):
    print(number1, number2, oper)
    if oper == '+':
        return number1 + number2
    if oper == '-':
        return number1 - number2
    if oper == '*':
        return number1 * number2
    if oper == '/':
        if number2 != 0:
            return number1 / number2
        else:
            print('вы ввели ноль!')
            print('введите другое число')
            return 0

    if oper == '**':
        return number1 ** number2
    if oper == '//':
        return number1 // number2
    if oper == '**2':
        return number1 **2
    if oper == '%':
        return number1 % number2


result = Calculeit(10, 5, '+')
print(result)
result = Calculeit(19, -21, '+')
print(result)
result = Calculeit(19, -21, '-')
print(result)
result = Calculeit(19, -21, '*')
print(result)
result = Calculeit(19, -21, '/')
print(result)
result = Calculeit(12, 2, '**')
print(result)
result = Calculeit(19, -21, '//')
print(result)
result = Calculeit(19, -21, '**2')
print(result)
result = Calculeit(19, -21, '%')
print(result)