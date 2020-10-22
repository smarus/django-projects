from _collections import deque

n = input()
deq = deque()
for i in range(int(n)):
    ins = input()
    if ins == 'SOLVED' and len(deq) > 0:
        deq.pop()
    else:
        deq.appendleft(ins)

for i in range(len(deq)):
    print(deq.pop().split(" ")[1])
