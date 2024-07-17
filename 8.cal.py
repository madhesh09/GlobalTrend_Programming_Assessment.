def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator,pls choose the valid operator"

try:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    operator = input("Enter any one of the operator (+, -, *, /): ")
    
    result = calculate(n1, n2, operator)
    print(result)
except ValueError:
    print("Error: Invalid input. Please enter numbers.")
