import random

def flip() -> bool:
    return random.random() > 0.5

def main():
    best = []
    for _ in range(10000):
        total = 0
        bet = random.random()
        while bet < 0.999:
            bet = random.random()
        for _ in range(1000):
            if flip():
                total += bet * 2

            else:
                total -= bet

        # if total > 10**9:
        best.append((total, bet))


    return sorted(best) 


print(main())
