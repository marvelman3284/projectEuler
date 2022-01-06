def main():

    num = 1000000
    seqLength = 0
    startingNum = 0
    seq = 0

    for i in range(2, num):
        length = 1
        seq = i 
        while seq != 1:
            if seq % 2 == 0:
                seq /= 2
            else:
                seq = seq * 3 + 1

            length += 1

        if length > seqLength:
            seqLength = length
            startingNum = i

    return startingNum, seqLength

print(main())
