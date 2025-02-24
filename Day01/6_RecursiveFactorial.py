def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial(n - 1)
    else:
        raise ValueError("Factorial is not defined for negative numbers.")


print(factorial(5))
print(factorial(3))
print(factorial(0))