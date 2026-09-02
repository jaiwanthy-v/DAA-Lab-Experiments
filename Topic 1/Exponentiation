def power(x, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        half = power(x, n // 2)
        return half * half

    return x * power(x, n - 1)


x = 2
n = 10

print("Result:", power(x, n))
