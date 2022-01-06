import math


def is_prime(n: float) -> bool:
    if n == 0 or n == 1:
        return False

    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


def primes(length: int) -> list[int]:
    primes = []
    for i in range(length):
        if is_prime(i):
            primes.append(i)

    return primes

def add_primes(primes, switch, num) -> tuple[int, int]:
    in_counter = 0
    sum = 0
    L = []
    while sum < num:
        sum = sum + primes[switch]
        if is_prime(sum):
            L.append(sum)
        in_counter += 1 
        switch += 1
    if L[-1] < num:
        return L[-1], in_counter
    else:
        return L[-2], in_counter


def main():
    prime = primes(1000000)
    main_counter = 0
    for switch in range(0, 10):
        x = add_primes(prime, switch, 1000000)
        print(x[0], x[1])
        if x[0] > main_counter:
            main_counter = x[0]
    print("Answer =", main_counter)


print(main())
