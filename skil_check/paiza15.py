""

""

human_song_len=input().rstrip().split(" ")
human_song_len=list(map(int,human_song_len))
ok=[]
for i in range(human_song_len[1]):
    ok.append(int(input()))
    # ok=list(map(int,ok))
# print(ok)
max_point=0
for i in range(human_song_len[0]):
    total_minus = []
    for j in range(human_song_len[1]):

        sabun=ok[j]-int(input())
        if sabun < 0:
            sabun = -sabun
        if sabun <= 5:
            minus =0
        elif sabun <= 10:
            minus = 1
        elif sabun <= 20:
            minus = 2
        elif sabun<=30:
            minus = 3
        else:
            minus=5
        total_minus.append(minus)
    point=100-sum(total_minus)
    if point >=max_point:
        max_point=point
print(max_point)




#
#
# singed_1=[]
# for i in range(int(human_songlengs[1])*int(human_songlengs[0])):
#     singed_1.append(input())
#     singed_1 = list(map(int, singed_1))
# print(singed_1)
# s=[]
# for i in range(int(human_songlengs[1])):
#     v=int(ok[i]-singed_1[i])
#     s.append(v)
# print(v)
# score=[]
# for i in range(0,int(human_songlengs[0])):
#     for j in range(int(human_songlengs[1])):
#         s=ok[j]-singed_1[j]
#         if s<0:
#             s=-s
#         if s>=20:
#             score=+20
#         elif s>=10:
#             score=+10
#         else:
#             s=0
#         print("スコア"+str(s))
#



# singed_2=[]
# for i in range(int(human_songlengs[1])):
#     singed_2.append(input())
# print(singed_2)