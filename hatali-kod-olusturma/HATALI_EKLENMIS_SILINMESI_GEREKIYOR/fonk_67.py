def function( *args_list ):
ans = []
for l in args_list:
ans.append( l.upper() )
return ans
object = function('Python', 'Functions', 'tutorial')
print( object )
def function( **kargs_list ):
ans = []
for key, value in kargs_list.items():
=
ans.append([key, value])
return ans
object = function(First = "Python", Second = "Functions", Third = "Tutorial")
print(object)