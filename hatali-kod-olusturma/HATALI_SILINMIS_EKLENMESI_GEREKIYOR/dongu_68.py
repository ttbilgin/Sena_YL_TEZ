nums = [1, 2, 3, 4, 5, 
n = 2
found = False
for num in nums:
    if n == num:
        found = True
        break
print(f'List contains {n}: {found}')
