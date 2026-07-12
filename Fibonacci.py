def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

n = 6

print("Fibonacci:")
for i in range(n):
    print(fibo(i), end=" ")
