def digitSum(n):
    dsum = 0
    for ele in sr(n):
        dsum += int(ele)
    return dsum
List = [367, 111, 562, 945, 6726, 873]
newList = [digitSum(i) for i in List if (i & 1)]
print(newList)
