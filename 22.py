print('x z w y')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (((w <= x) or (y <= z)) and ((x == y) <= (w == z))) == 0:
                    print(x, z, w, y)