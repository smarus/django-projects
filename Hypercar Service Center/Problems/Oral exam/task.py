import collections

queue = collections.deque()

for _ in range(int(input())):
    line = input().split()
    if len(line) > 1:
        queue.appendleft(line[1])
    elif line[0] == 'EXTRA':
        queue.appendleft(queue[len(queue) - 1])
        queue.pop()
    else:
        print(queue.pop())
for _ in queue:
    print(_)
