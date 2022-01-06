
def almost():
    sum = 0
    for i in range(1000000000):
        perm = i + i + (i + 1)
        if perm > 1000000000:
            break
        sum += perm

    print(sum) 

almost()
