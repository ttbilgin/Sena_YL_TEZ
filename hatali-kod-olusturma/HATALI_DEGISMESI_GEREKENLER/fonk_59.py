def myFun(arg1, *argv):
    prnt('First argument :', arg1)
    for arg in argv:
        print('Next argument through *argv :', arg)
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
