m = int(input())#старт
p = int(input())#увеличение
n = int(input())#колво дней
i = 0
for i in range(n):
    i = i +1
    m = m + m * p / 100
    print(i, m)