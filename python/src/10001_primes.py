# Problem 5

import math

def is_prime(n: float) -> bool:
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


primes = []

for i in range(1000000):
    if is_prime(i): primes.append(i)

print(primes[10002])
