count = 0
for n1 in 'МИТРОФАН':
    for n2 in '012345678':
        for n3 in '012345678':
            for n4 in '012345678':
                for n5 in '012345678':
                    for n6 in '012345678':
                        for n7 in '012345678':
                            n = f'{n1}{n2}{n3}{n4}{n5}{n6}{n7}'
                            if n.count('6') == 1:
                                odd_count = 0
                                for odd in '1357':
                                    odd_count += n.count(odd)
                                if odd_count == 2:
                                    count += 1
print(count)





