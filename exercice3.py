import mathlib
target = 600851475143

prime_decomp = [1]
primesgen = mathlib.primes(int(target**0.5))
rest = target
while rest > 1:
    nextprime = next(primesgen)
    while rest % nextprime == 0:
        rest = rest / nextprime
        prime_decomp.append(nextprime)
print(prime_decomp[-1])
