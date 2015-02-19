def _primes():
    seq = []
    yield 2
    yield 3
    i = 1
    while True:
        i += 4
        if all(map(lambda x:i % x != 0, (el for el in seq if el <= i**0.5))):
            yield i
            seq.append(i)
        i += 2
        if all(map(lambda x:i % x != 0, (el for el in seq if el <= i**0.5))):
            yield i
            seq.append(i)

def primes(maximum=float('inf'), nb_max=float('inf')):
    primesgenerator = _primes()
    nextprime = next(primesgenerator)
    nb = 0
    while nb < nb_max and nextprime < maximum:
        yield nextprime
        nb += 1
        nextprime = next(primesgenerator)

def factorize(integer):
    factorization = []
    primesgenerator = primes(integer+1)
    while integer > 1:
        nextprime = next(primesgenerator)
        while integer % nextprime == 0:
            integer = integer / nextprime
            factorization.append(nextprime)
    return factorization
