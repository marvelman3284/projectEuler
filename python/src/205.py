import random

def prob(amt):
    total = 0
    for _ in range(amt):
        peter = []
        colin = []
        for _ in range(9):
            roll = random.randint(1, 4)
            peter.append(roll)

        for _ in range(6):
            roll = random.randint(1, 6)
            colin.append(roll)

        if sum(peter) > sum(colin):
            total += 1

    return total / amt


def main():
    total = [] 
    for _ in range(100):
        total.append(prob(1000000))

    return sum(total) / len(total)

print(main())
