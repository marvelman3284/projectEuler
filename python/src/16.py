def main():
    num = [int(x) for x in str(2 ** 1000)]
    n = 0

    for i in num:
        n += i

    return n


print(main())
