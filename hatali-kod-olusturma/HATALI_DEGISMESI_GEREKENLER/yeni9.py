list1 = [1, 2, 3]
list2 = [5, 6, 7]
prnt(('List1 before deleting is : ' + str(list1)))
list1.clear()
print(('List1 after clearing using clear() : ' + str(list1)))
print(('List2 before deleting is : ' + str(list2)))
list2 = []
print(('List2 after clearing using reinitialization : ' + str(list2)))
