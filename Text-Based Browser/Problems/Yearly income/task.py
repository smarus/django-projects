# write your code here
with open('salary.txt') as f1 ,\
     open('salary_year.txt', 'w') as f2:
    for file in f1.readlines():
        value = int(file.rstrip('\n'))
        f2.write(str(value * 12))
        f2.write('\n')



