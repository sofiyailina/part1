'''На вход алгоритма подаётся два натуральных числа N и M. Алгоритм строит по ним новое число R следующим образом.
1) Вычисляется число SN как квадрат суммы цифр двоичной записи числа N.
2) Вычисляется число SM как квадрат суммы цифр двоичной записи числа M.
3) Результат R вычисляется как SN – SM.
Укажите минимальную сумму чисел N и M, при которых получается R = 33.'''

def algo(n, m):
    nbin = bin(n)[2:]
    mbin = bin(m)[2:]
    sn = 0
    for digit in nbin:
        sn += int(digit)
    sn = sn ** 2
    sm = 0
    for digit in mbin:
        sm += int(digit)
    sm = sm ** 2
    r = sn - sm
    return r

minsum = 10**10
for n in range(1,200):
    for m in range(1,200):
        if algo(n, m) == 33:
            minsum = min(minsum, n+m)
print(minsum)
            