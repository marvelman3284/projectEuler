def main():
    num = 10000000
    total = 0

    for i in range(1, num+1):
        print(f"starting: {i}")
        sum = i
        while sum != 1 or sum != 89:
            digets = [int(n) for n in str(sum)]
            sum = 0
            for j in digets:
                j = j ** 2
                sum += j
            print(sum)


            if sum == 89:
                total += 1
                break

            elif sum == 1:
                break

    return total


print("\n\n\n", main())
