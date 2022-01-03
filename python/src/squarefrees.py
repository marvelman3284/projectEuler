def get_perfects(n: int, k:int) -> list[int]:
    squares = []
    for i in range(n**k):
        squares.append(i**2)

    return squares

print(get_perfects(2, 50))
