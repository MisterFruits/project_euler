def primes(max):
    seq = []
    yield 2
    for i in range(3,max,2):
        if all(map(lambda x:i % x != 0, (el for el in seq if el**0.5 < i))):
            yield i
            seq.append(i)

def factorize(integer):
    factorization = []
    primesgenerator = primes(int(integer**0.5))
    while integer > 1:
        nextprime = next(primesgenerator)
        while integer % nextprime == 0:
            integer = integer / nextprime
            factorization.append(nextprime)
    return factorization
