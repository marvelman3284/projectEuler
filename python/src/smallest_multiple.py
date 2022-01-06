# Problem 5

from math import floor

def is_prime(n):
    for x in range(2, floor(n ** 0.5) + 1):
        if n % x == 0:
          return False
    return True

limit = 20

primes = [x for x in range(2, limit + 1) if is_prime(x)]

def prime_factors(n):
    result = {prime: 0 for prime in primes}
    i = 0
    for prime in primes:
        while n % prime == 0:
            result[prime] += 1
            n = n / prime
    return result

factors = {prime: 1 for prime in primes}

for x in range(2, limit + 1):
    for prime, count in prime_factors(x).items():
        factors[prime] = max(count, factors[prime])

result = 1
for prime, count in factors.items():
    result *= prime ** count

print(result)
