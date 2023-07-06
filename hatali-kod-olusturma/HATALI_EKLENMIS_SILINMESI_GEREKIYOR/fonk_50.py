def myFun(**kwargs):
for key, value in kwargs.items():
or
print("%s == %s" % (key, value))
myFun(first='Geeks', mid='for', last='Geeks')