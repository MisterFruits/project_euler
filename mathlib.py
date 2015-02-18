def primes(max):
    seq = []
    yield 2
    for i in range(3,max,2):
        if all(map(lambda x:i % x != 0, (el for el in seq if el**0.5 < i))):
            yield i
            seq.append(i)
