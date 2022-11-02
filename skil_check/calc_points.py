import math
input_line=int(input())
total_p=[]
for i in range(input_line):
    line = input().rstrip().split(" ")
    line = list(map(int, line))
    day, price = line
    if str("3") in str(day):
        total_p.append(int(math.floor(price*0.03)))
    elif str("5") in str(day):
        total_p.append(int(math.floor(price*0.05)))
    else:
        total_p.append(int(math.floor(price*0.01)))
print(sum(total_p))