def square( item_list ):    
    'This function will find the square  items in the list'  
    squares = [ ]    
    for l in item_list:    
        squares.append( l**2 )    
    return squares       
my_list = [17, 52, 8];    
my_result = square( my_list )    
print( "Squares of the list are: ", my_result )    