def sum_squares():
    sum = 0
    for i in range(101):
        sum += i*i

    return sum

def square_sum():
    sum = 0
    for i in range(101):
        sum += i

    return sum*sum


if __name__ == "__main__":
   squares = sum_squares()
   sums = square_sum()
   print(sums-squares)
