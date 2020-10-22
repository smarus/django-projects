# put your python code here
my_stack = []

n = input()
b = False
for i in range(len(n)):
    if i == 0 and n[i] ==')':
        b = True
        break
    if n[i] == '(' or n[i] == ')':
        if n[i] == ')' and len(my_stack) > 0:
            my_stack.pop()
        elif n[i] == '(':
            my_stack.append(n[i])
        else:
            b = True
            break
if len(my_stack) == 0 and not b:
    print("OK")
else:
    print("ERROR")

