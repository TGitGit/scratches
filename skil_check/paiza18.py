import itertools
dis=input().rstrip().split()
total_room=input().rstrip().split()
room_num=[]
for i in range(int(total_room[0])):
    room_num.append(input().rstrip().split("\n"))
    # room_num.append(num)
# print(room_num)
room_num=list(itertools.chain.from_iterable(room_num))
none=0
for j in range(int(total_room[0])):
    if dis[0] in room_num[j]:
        none+=1

else:
        print(room_num[j])
if none==0:
    print("none")