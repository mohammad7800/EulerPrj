from time import time
t = time()
s = 998001


def check(inp):
    lst = list(str(inp))
    revers = lst.copy()
    revers.reverse()
    return lst == revers


while s > 0:
    if check(s):
        l = 999
        while l > 99:
            if s % l == 0:
                n = s / l
                if n > 99 and n < 1000:
                    print(s)
                    print(l)
                    print(s / l)
                    print(time() - t)
                    exit()
            l -= 1
    s -= 1

