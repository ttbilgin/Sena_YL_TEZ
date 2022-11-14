from moretkn import *

errorcode="""
def say_hello():
	print()
say_hello()
if 
for
"""

deneme=call_moretokenizer(errorcode)

print(deneme)

list1=[]
for i in TOKENS:
    list1.append(i[1])
print(list1)

keywords_tokens_list=list1+UPPER_KEYWORDS
print(keywords_tokens_list)

list_ind= []
for item in deneme:
    index=keywords_tokens_list.index(item)
    list_ind.append(index)

print(list_ind)
