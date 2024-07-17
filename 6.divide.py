def divide(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error:your entered number is invalid!. Enter the number."
    return result

n1 = 10
n2 = 5
print(divide(n1, n2))
