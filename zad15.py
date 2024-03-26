def DEL(n, m):
    return n % m ==0

def f(x, A):
    return ((DEL(x, 2) <= (not DEL(x, 3))) or (x + A >= 100))

for A in range(1, 100000):
    flag = True
    for x in range(1, 1000):
        if not f(x, A):
            flag = False
            break
    if flag:
        print(A)
        break