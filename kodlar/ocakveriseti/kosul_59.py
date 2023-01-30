nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nums_less_3_greater_equal_10_multiple_2 = []

for num in nums:
    if num < 3 or num >= 10 and num % 2 == 0:
        nums_less_3_greater_equal_10_multiple_2.append(num)

print(nums_less_3_greater_equal_10_multiple_2)