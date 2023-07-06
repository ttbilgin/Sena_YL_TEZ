def my_var_sum(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
sum = my_var_sum(99,10,54,23)
print(f"The numbers that you have add up to {sum}")
sum = my_var_sum(9,87,45)
print(f"The numbers that you have add up to {sum}")
sum = my_var_sum(5,21,36,79,45,65)
print(f"The numbers that you have add up to {sum}")
