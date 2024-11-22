with open ('codingal.txt','w') as file:
    file.write("hello there i see you")
file.close()

with open('codingal.txt','r') as file:
    data=file.readlines()
    print('words in the file are....')
    for line in data:
        word=line.split()
        print(word)
file.close()