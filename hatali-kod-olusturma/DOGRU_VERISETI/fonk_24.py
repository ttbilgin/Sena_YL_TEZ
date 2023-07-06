def find_sum(*numbers):
    result = 0   
    for num in numbers:
        result = result + num   
    print("Sum = ", result)
find_sum(1, 2, 3)
find_sum(4, 9)