import math
from functools import reduce

def is_prime(n: float) -> bool:
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def semi_primes(l: set):
    s = set()
    for i in l:
        if is_prime(i): s.add(i)

    return s


ls = factors(10000000)
print(semi_primes(ls))
