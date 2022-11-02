line=input().rstrip().split(" ")
time_pay=list(map(int,line))
day,night,midnight=time_pay

work_day=int(input())
day_work=[]
night_work=[]
midnight_work=[]
for _ in range(work_day):
    line = input().rstrip().split(" ")
    work_time = list(map(int, line))
    start,end = work_time

    for i in range(start,end):
        if 9 <= i <= 16:
            day_work.append(day)
        elif 17 <= i <= 21:
            night_work.append(night)
        else:
            midnight_work.append(midnight)
print(sum(day_work+night_work+midnight_work))
