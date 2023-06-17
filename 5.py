print('A x y')
for A in range(1, 1000):
    test = True
    for x in range(1,1000):
        if not ((A < 50) and ((x % A != 0) <= ((x % 10 == 0) <= (x % 18 != 0)))):
            test = False
            break
    if test:
        print(A)

