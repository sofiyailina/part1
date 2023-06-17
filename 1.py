print('A x y')
for A in range(1, 100):
    test = True
    for x in range(1,100):
        for y in range(1,100):
            if not (((2*x) + (3*y) !=60) or (A >= x) or (A >= y)):
                test = False
                break
    if test:
        print(A)
        break

