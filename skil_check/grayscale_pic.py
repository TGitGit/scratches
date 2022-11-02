import statistics
import itertools
line=input().rstrip().split(" ")
time_pay=list(map(int,line))
n,k=time_pay
new_scale=n/k
pic=[]
for _ in range(n):
    line = input().rstrip().split(" ")
    row = list(map(int, line))
    pic.append(row)
result=[]
temp=[]
for math in range(int(pow(n/k,2))):
    temp = []
    for r in range(int(n / k)+1):

        # for c in range(int(n / k)+1):
        # pic[r][:k]
        temp.append(pic[math][:k])
    temp=list(itertools.chain.from_iterable(temp))
    result.append(statistics.mean(temp))
print(result)