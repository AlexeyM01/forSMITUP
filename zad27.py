f = open('27_B.txt')
n, summ = 89, 0
mins = {0: (0, 0)}
ans = 0
l = 0
for i in range(1, int(f.readline())+1):
    summ += int(f.readline())
    if summ % n in mins:
        if summ - mins[summ % n][0] > ans:
            ans = summ - mins[summ % n][0]
            l = i - mins[summ % n][1]
    else:
        mins[summ % n] = (summ, i)
print(l)