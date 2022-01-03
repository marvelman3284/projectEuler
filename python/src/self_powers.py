def self_powers():
    sum = 0
    for i in range(1, 1000):
        sum += i**i

    sum = str(sum)

    return sum[-10:]


print(self_powers())
