import math

def main():
    prod = math.factorial(100)
    sum = 0  

    print(prod)

    for i in str(prod):
        sum += int(i)

    return sum

print(main())
