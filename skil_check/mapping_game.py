import itertools
input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))
turn,row,column=input_line
#任意の長さのリストを作る(中身はNone)
bord=list([None])*(row*column)
#1次元リストを2次元リストにする関数(カラム数を指定するとロウ数は自動的に決まる)
def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]
bord=convert_1d_to_2d(bord,column)

for i in range(turn*3):
    player=i%3
    input_line = input().rstrip().split(" ")
    input_line = list(map(int, input_line))
    x, y, mas = input_line
    if player==0:

        for r in range(x,mas+x):
            for c in range(y,mas+y):
                try:
                    if bord[c][r]==None :
                        bord[c][r]="R"

                    elif bord[c][r]=="B":
                        bord[c][r]="G"
                    elif bord[c][r]=="G":
                        bord[c][r]="B"

                except:pass

    if player == 1:
        for r in range(x,mas+x):
            for c in range(y,mas+y):
                try:

                    if bord[c][r] == None:
                        bord[c][r] = "B"
                    elif bord[c][r] == "R":
                        bord[c][r] = "G"
                    elif bord[c][r] == "G":
                        bord[c][r] = "R"
                except:pass

    if player == 2:
        for r in range(x,mas+x):
            for c in range(y,mas+y):
                try:

                    if bord[c][r] == None:
                        bord[c][r] = "G"
                    elif bord[c][r] == "R":
                        bord[c][r] = "B"
                    elif bord[c][r] == "B":
                        bord[c][r] = "R"
                except:pass
#2次元リストを1次元にする(import itertoolsが必要
flat_bord=list(itertools.chain.from_iterable(bord))
count_red=(flat_bord.count("R"))
count_blue=(flat_bord.count("B"))
count_green=(flat_bord.count("G"))

print(count_red,count_blue,count_green,sep=" ")
