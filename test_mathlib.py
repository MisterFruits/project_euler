from mathlib import primes, factorize

def test_primes():
    assert [el for el in primes(0)] == []
    assert [el for el in primes(1)] == []
    assert [el for el in primes(2)] == []
    assert [el for el in primes(3)] == [2]
    assert [el for el in primes(5)] == [2, 3]
    assert [el for el in primes(10)] == [2, 3, 5, 7]

    assert [el for el in primes(maximum=0)] == []
    assert [el for el in primes(maximum=1)] == []
    assert [el for el in primes(maximum=2)] == []
    assert [el for el in primes(maximum=3)] == [2]
    assert [el for el in primes(maximum=5)] == [2, 3]
    assert [el for el in primes(maximum=10)] == [2, 3, 5, 7]

    assert len([el for el in primes(nb_max=0)]) == 0
    assert len([el for el in primes(nb_max=1)]) == 1
    assert len([el for el in primes(nb_max=2)]) == 2
    assert len([el for el in primes(nb_max=3)]) == 3
    assert len([el for el in primes(nb_max=5)]) == 5
    assert len([el for el in primes(nb_max=10)]) == 10

    assert [el for el in primes(maximum=10, nb_max=2)] == [2, 3]
    assert [el for el in primes(maximum=3, nb_max=100)] == [2]

    assert [el for el in primes(nb_max=10001)][-1] == 104743


def test_factorize():
    assert factorize(5) == [5]
    assert factorize(25) == [5, 5]
    assert factorize(125) == [5, 5, 5]
    assert factorize(360) == [2, 2, 2, 3, 3, 5]
    assert factorize(1001) == [7, 11, 13]
    assert factorize(1010021) == [17, 19, 53, 59]
