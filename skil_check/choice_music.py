line = input().rstrip().split(" ")
line = list(map(int, line))
music,mx_m,mx_y = line
mx_time=mx_m*60+mx_y

music_time=[]
for i in range(music):
    line = input().rstrip().split(" ")
    line = list(map(int, line))
    m, y = line
    music_time.append(m*60+y)
s_music_time=sorted(music_time)

for i in range(1,len(s_music_time)+1):
    if s_music_time[0]>=mx_time:
        print(0)
        break
    elif sum(s_music_time[0:i])>=mx_time:
        print(i-1)
        break
else:print(len(s_music_time))