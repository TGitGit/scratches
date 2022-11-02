#席替えの席決め
card=input().rstrip().split(" ")
cards=list(map(int,card))
row,column,std=cards
#1次元リストを2次元にする
def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]

seat=[0]*(row*column)
for i in range(std):
    input_line = int(input())
    seat[input_line-1]=i+1

new=convert_1d_to_2d(seat,column)
# 2次元リストの行列を入れ替える
l_2d_t = [list(x) for x in zip(*new)]
for r in range(column):
    count = l_2d_t[r].count(0)
    while 0 in l_2d_t[r]:
        l_2d_t[r].remove(0)
    for i in range(count):
        l_2d_t[r].append(0)
# 2次元リストの行列を入れ替える(元に戻す)
ok = [list(x) for x in zip(*l_2d_t)]
for i in range(row):

    s=ok[i]
    print(*s,sep=" ")