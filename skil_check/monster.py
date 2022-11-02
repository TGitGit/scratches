line = input().rstrip().split(" ")
line = list(map(int, line))
atk,dfc,spd = line

evo_num=int(input())
flag=False
for i in range(evo_num):
    line = input().rstrip().split(" ")
    para = list(map(int, line[1:]))
    min_atk,mx_atk, min_dfc,mx_dfc, min_spd,mx_spd = para
    monster_name=str(line[0])

    if min_atk<=atk<=mx_atk and min_dfc<=dfc<=mx_dfc and min_spd<=spd<=mx_spd:
        print(monster_name)
        flag=True
if not flag:
    print("no evolution")