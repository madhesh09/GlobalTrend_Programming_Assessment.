def fib(n):
    if n <= 0:
        return "Pls enter the Positive Value."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = 5
print(f"The {n}th Fibonacci number is: {fib(n)}")

