# read sums.txfdsf
files = open("sums.txt", 'r')
for file in files.readlines():
    a, b = file.split(" ")
    print(int(a) + int(b))

files.close()
