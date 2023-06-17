num = int(input())
n_1 = (num % pow(10, 4)) // pow(10, 4-1)
n_2 = (num % pow(10, 4-1)) // pow(10, 4-2)
n_3 = (num % pow(10, 2)) // pow(10, 1)
n_4 = (num % pow(10, 1)) // pow(10, 0)
sum_1 = n_1 + n_2
sum_2 = n_2 + n_3
sum_3 = n_3 + n_4
