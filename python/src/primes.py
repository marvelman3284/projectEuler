# Problem 3

import math
import time

start = time.perf_counter()
def largest_prime_factor(n: int) -> list[int]:
    factors = []
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if is_prime(x):
            if n % x == 0:
                pair = n / x
                factors.append(x)
                if is_prime(pair):
                  factors.append(pair)
    return sorted(factors)[-1]

def is_prime(n: float) -> bool:
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


print(largest_prime_factor(600851475143))
print(f"Time taken: {time.perf_counter() - start}")
