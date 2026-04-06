def calculate(num1, num2, operation):
    # print(num1, num2, operation)
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "**":
        return num1 ** num2
    # if operation == "%":
    #     return num1 % num2
    if operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print("на нуль делить нельзя")
            return print("введите другое число")
    if operation == "//":
        if num2 != 0:
            return num1 // num2
        else:
            print("на нуль делить нельзя")
            return print("введите другое число")

result = calculate(10, 13, "+")
print(result)

result = calculate(5, 13, "-")
print(result)

result = calculate(5, 13, "*")
print(result)

result = calculate(13, 2, "**")
print(result)

# result = calculate(5, 2, "%")
# print(result)

result = calculate(5, 0, "/")
print(result)

result = calculate(5, 2, "//")
print(result)