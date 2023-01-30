from moretokenizer import *
import os
directory = 'ocakveriseti'

def listToString(lines):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in lines:
        str1 += ele
 
    # return string
    return str1
with open('output_karisik.txt', 'w') as output_file:
  # Iterate through all files in the directory
  for filename in os.listdir(directory):
    # Check if the file is a Python file
    if filename.endswith('.py'):
      # Open the file and read its contents
      with open(os.path.join(directory, filename), 'r') as file:
         lines = file.read()
        # Write the contents of the file to the output file
      for item in list_ind:
            
            output_file.write("%d " % item)
      errorcode = listToString(lines)
      deneme=call_moretokenizer(errorcode)
      output_file.write("\n")
      print(deneme)


      list1=[]
      for i in TOKENS:
        list1.append(i[1])

      keywords_tokens_list=list1+UPPER_KEYWORDS

      list_ind= []
      for item in deneme:
        index=keywords_tokens_list.index(item)
        list_ind.append(index)

      print(list_ind)







