def digitSum(n):
	dsum = 0
	for ele in str(n):
		dsum += int(ele)
	return dsum

List = [367, 111, 562, 945,  873]
newList = [digitSum(i) for i in List if i & 1]
print(newList)
