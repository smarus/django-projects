# use the function blackbox(lst) that is already defined
lst = [1 , 2 ,3]
get_list = blackbox(lst)
if lst is get_list:
    print("modifies")
else:
    print("new")