test_dict = {'Gfg' : {'is' : 'best'}}
print("The original dictionary is : " + str(test_dict))
res = test_dict.get('Gfg', {}).get('is')
print("The nested safely accessed value is : " + str(res))
