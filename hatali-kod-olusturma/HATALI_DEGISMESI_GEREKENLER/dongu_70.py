def print_sum_even_nums(even_nums):
    total = 0
    for x in even_nums:
        if ((x % 2) != 0):
            break
        total += x
    else:
        print('For loop executed normally')
        print(f'Sum of numbers {total}')
print_sum_even_nums([2, 4, 6, 8])
print_sum_even_nums([2, 4, 5, 8])
