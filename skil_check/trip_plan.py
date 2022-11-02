meisho = int(input())
meisho_time=[]
for i in range(meisho):
    time= int(input())
    meisho_time.append(time)

ido_time=[]
for i in range(meisho):
    time=input().rstrip().split(" ")
    time=list(map(int,time))
    ido_time.append(time)

go_num=int(input())
junban=[]
for i in range(go_num):
    time = int(input())
    junban.append(time)
print(junban)
result=0
for i in range(go_num):
    print(junban[i]-1)
    print(junban[i])
    result+=ido_time[junban[i]-1][junban[i]]