n = int(input())
read = []
unread = []
for i in range(n):
    r = input()
    is_buy = r.split(" ")
    if is_buy[0] == "BUY":
        unread.append(" ".join(is_buy[1:len(is_buy)]))
    else:
        read.append(unread.pop())

for i in read:
    print(i)

