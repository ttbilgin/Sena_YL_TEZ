list_of_numbers = [4,5,9,17,21]
for i in list_of_numbers:
    if i%2!=0:
        if i%3==0:
            print (i,"is an odd number & divisible by 
        else:
            print (i, "is an odd number but not divisible by 3")
    else:
        print(i,"is an even number")