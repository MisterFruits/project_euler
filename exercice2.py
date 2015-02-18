fib = [1, 2]
while fib[-1] < 4000000:
    fib.append(fib[-1] + fib[-2])

print(sum((el for el in fib if el % 2 == 0)))
