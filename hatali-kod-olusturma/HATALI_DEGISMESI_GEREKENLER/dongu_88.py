numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8]
sum_ = 0
for num in rng(len(numbers)):
    sum_ = (sum_ + (numbers[num] ** 2))
print('The sum of squares is: ', sum_)
