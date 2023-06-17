def algo(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + '01'
    else:
        b = b + '10'
    r = int(b, 2)
    return r

for n in range(1, 1000):
    if algo(n) > 97:
        print(n)
        break