line = input().rstrip().split(" ")
line = list(map(int, line))
xc, yc,r1,r2 = line

human = int(input())

for i in range(human):
    l = input().rstrip().split(" ")
    l = list(map(int, l))
    x1, y1 = l
    if r1**2<=(x1-xc)**2+(y1-yc)**2<=(r2**2):
        print("yes")
    else:print("no")