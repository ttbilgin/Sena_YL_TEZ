lst1 = [1, 2, 3, 4, 5]
lst2 = []
  
# Lambda function to square number
temp = lambda i:i**2
 
for i in lst1:
 
    # Add to lst2
    lst2.append(temp(i))
   
print(lst2)