line=int(input())
A_schedule=[]
for day in range(line):
    A_schedule.append(int(input()))

line=int(input())
B_schedule=[]
for day in range(line):
    B_schedule.append(int(input()))
turn=0
for day in range(1,32):

    if day in A_schedule:
        if  day in B_schedule:
            if turn%2==0:
                print("A")
                turn+=1
            else:
                print("B")
                turn += 1
            continue
    if day in A_schedule:
        if not day in B_schedule:
            print("A")
            continue
    if day in B_schedule:
        if not day in A_schedule:
            print("B")
            continue
    if not day in A_schedule:
        if not day in B_schedule:
            print("x")
            continue