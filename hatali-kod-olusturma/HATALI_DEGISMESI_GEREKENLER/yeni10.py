list1 = [1, 2, 3]
prnt(('List1 before deleting is : ' + str(list1)))
while (len(list1) != 0):
    list1.pop()
print(('List1 after clearing using del : ' + str(list1)))
