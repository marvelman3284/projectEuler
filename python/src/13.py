def main():
    total = 0
    with open('num.txt', 'r') as f:
        l = [line.strip('\n') for line in f.readlines()]

    for i in l:
        total += int(i)


    # print(l)
    print(str(total)[:10])

main()
