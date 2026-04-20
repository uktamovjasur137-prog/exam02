def calculate(num1: float, num2: float, operator: str):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "0 ga bolib bolmaydi"
        return num1 / num2
    else:
        return "Notogri amal"


print(calculate(3, 3, "+"))