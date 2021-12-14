# Problem 4

import time

def palindrome_product() -> int:
    prods = []
    prod = ""
    for i in range(100, 999, 1):
        for j in range(100, 999, 1):
            prod = str(i * j)
            if prod == prod[::-1]:
                prods.append(int(prod))

    return sorted(prods)[-1]


if __name__ == "__main__":
    start = time.perf_counter()
    euler = palindrome_product()
    print(euler)
    print(f"Time taken {time.perf_counter()-start}")
