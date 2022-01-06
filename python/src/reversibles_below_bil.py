def reversibles() -> list[int]:
    reversible = []
    for i in range(1001, 1000000000, 2):
        j = reverse(i)
        k = j + i
        l = reverse(k)


        if k == l and l % 2 == 1:
            reversible.append((i, j))


    return reversible

def reverse(n) -> int:
    n = str(n)
    return int(n[::-1])


print(len(reversibles()))
