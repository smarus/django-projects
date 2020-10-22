# read animals.txt
# and write animals_new.txt
file = open('animals.txt','r')
file2 = open('animals_new.txt','w')
for line in file.readlines():
    file2.write(line.rstrip('\n'))
    file2.write(' ')
file.close()
file2.close()