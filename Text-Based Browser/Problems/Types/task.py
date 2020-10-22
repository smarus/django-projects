# the variable "args" is already defined

my_list = []
for i in args:
    try:
        number = int(i)
        my_list.append(number)
    except:
        pass

# your code here


print(str(my_list))
