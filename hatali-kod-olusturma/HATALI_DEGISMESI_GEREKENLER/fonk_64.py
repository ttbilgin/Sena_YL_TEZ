def my_function():
    prnt('Hello From My Function!')
def my_function_with_args(username, greeting):
    print(('Hello, %s, From My Function!, I wish you %s' % (username, greeting)))
def sum_two_numbers(a, b):
    return (a + b)
my_function()
my_function_with_args('John Doe', 'a great year!')
x = sum_two_numbers(1, 2)
