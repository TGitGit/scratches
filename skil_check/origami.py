input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))
paper,centi=input_line

l=0
l+=centi
for i in range(paper-1):
    input_line = int(input())
    a=centi-input_line
    l+=a
ans=centi*l
print(ans)