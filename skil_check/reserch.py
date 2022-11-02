input_line=input().rstrip().split(" ")
dis=list(map(int,input_line))
tree,bench_m=dis

input_line=input().rstrip().split(" ")
light=list(map(int,input_line))
input_line=int(input())
light.insert(0,0)

for i in range(input_line):
    start,end = input().rstrip().split(" ")
    start=int(start)
    end=int(end)+1

    ave=sum(light[start:end])/len(light[start:end])
    while bench_m>=ave:
        for i in range(start, end):
            light[i]=light[i]+1
        ave = sum(light[start:end]) / len(light[start:end])
else:
    light.pop(0)
    print(*light,sep=" ")
