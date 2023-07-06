nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nums_less_3_greater_equal_10 = []
for num in nums:
    if num < 3 and num >= 10:
        nums_less_3_greater_equal_10.append(num)
print(nums_less_3_greater_equal_10)