days = int(input())

now = []
for day in range(days):

    line = input().rstrip().split(" ")
    line = list(map(int,line))
    first,plane,arrive= line
    if arrive==(first+plane):
        now.append(first+plane+arrive)
    elif arrive>=(first+plane):
         now.append(24-(arrive-(first+plane)))
    else:
         temp=-(arrive-(first+plane))
         now.append(24 + temp)
print(min(now))
print(max(now))