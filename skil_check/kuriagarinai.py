line = input().rstrip().split(" ")
a,b= line

l_a=list(a)
l_b=list(b)
if len(l_a)<=len(l_b):
    while len(l_a) != len(l_b):
        l_a.insert(0,"0")
l_a=(list(map(int,l_a)))
if len(l_b)<=len(l_a):
    while len(l_b) != len(l_a):
        l_b.insert(0,"0")
l_b=(list(map(int,l_b)))


result=[]
for i in range(1,len(l_a)+1):
    sum_ab=l_a[-i]+l_b[-i]
    sum_ab=str(sum_ab)
    result.append(sum_ab[-1])

result.reverse()
print(*result,sep="")


