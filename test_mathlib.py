from mathlib import primes, factorize

def test_primes():
    assert [el for el in primes(0)] == []
    assert [el for el in primes(1)] == []
    assert [el for el in primes(2)] == []
    assert [el for el in primes(3)] == [2]
    assert [el for el in primes(5)] == [2, 3]
    assert [el for el in primes(10)] == [2, 3, 5, 7]

def test_factorize():
    assert factorize(5) == [5]
    assert factorize(25) == [5, 5]
    assert factorize(125) == [5, 5, 5]
    assert factorize(360) == [2, 2, 2, 3, 3, 5]
    assert factorize(1001) == [7, 11, 13]
    assert factorize(1010021) == [17, 19, 53, 59]
