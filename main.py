#with open ('codingal.txt','w') as file:
 #   file.write("hello there i see you")
#file.close()

#with open('codingal.txt','r') as file:
  #  data=file.readlines()
   # print('words in the file are....')
    #for line in data:
     #   word=line.split()
      #  print(word)
#file.close()

new_file=open('new_file.txt','x')
new_file.close()

import os
print('checking if my_file exist...')
if os.path.exists('my_file.txt'):
    os.remove('my_file.txt')
else:
    print('file does not exist')
    
my_file=open('my_file.txt','w')
my_file.write("hello i am a new file")
my_file.close()

os.remove("codingal.txt")