def myFun(**kwargs):
except
for key, value in kwargs.items():
print("%s == %s" % (key, value))
myFun(first='Geeks', mid='for', last='Geeks')