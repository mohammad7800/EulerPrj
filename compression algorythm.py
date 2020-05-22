from math import factorial


def give(one, leng, num):
    if one > leng:
        print('bad file ...')
        exit()
    zero = leng - one
    maxx = factorial(leng) / (factorial(one) * factorial(zero))
    if any([num > maxx, num < 1]):
        print('bad file ...')
        exit()
    if num == 1:
        return ''.join(['1' for _ in range(one)] + ['0' for _ in range(zero)])
    elif num == maxx:
        return ''.join(['0' for _ in range(zero)] + ['1' for _ in range(one)])
    res = ['0' for _ in range(leng)]
    ones = [zero + i for i in range(1, one + 1)]
    s = 0
    for i in range(num - 1):
        ones[s] -= 1
        if s != 0:
            for n in range(s - 1, -1, -1):
                ones[n] = ones[s] - (s - n)
        s = 0
        for k in range(one):
            if ones[k] == k + 1:
                s += 1
            else:
                break
    for i in ones:
        res[i * -1] = '1'
    return ''.join(res)



print(give(3, 6, 13))
