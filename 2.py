#print('x y z w')
#for x in range(2):
 #   for y in range(2):
  #      for z in range(2):
   #         for w in range(2):
    #            if ((w or not(x)) and (w == (not(y))) and (w <= z)) == 1:
     #               print(x, y, z, w)

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x <= y) == (y <= z)) and (y or w)) == 1:
                    print(x, y, z, w)
#xzy