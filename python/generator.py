def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
#creat fibonacci
fib = fibonacci(5)

#iterate and print the fibonacci number
for num in fib:
    print(num,end="")
