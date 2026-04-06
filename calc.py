def calculate(num1, num2, operation):
    # print(num1, num2, operation)
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2

result = calculate(10, 13, "+")
print(result)

result = calculate(5, 13, "-")
print(result)

