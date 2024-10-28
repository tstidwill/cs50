
def main():
    expression = input("Expression: ").split()
    num1 = float(expression[0])
    num2 = float(expression[2])
    operator = expression[1]

    if operator == "+":
        return num1+num2
    elif operator == "-":
        return num1-num2
    elif operator == "*":
        return num1*num2
    elif operator == "/":
        return num1/num2


print(main())


