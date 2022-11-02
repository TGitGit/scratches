"""
https://paiza.jp/works/challenges/506/retry
膨張と収縮を繰り返す
入力例1
7 7 2
.......
.#.###.
.####..
.##.##.
.####..
.......
......#
DE
"""

line = input().rstrip().split(" ")
line = list(map(int, line))
row, column,ope= line
#入力値を2次元リストに入れる
l_img=[]
for i in range(row):
    img = input()
    img = list(map(str, img))
    #out of index listのエラーに対応するため左右に1列ずつ余分に挿入する
    img.insert(0,".")
    img.append(".")
    l_img.append(img)
#out of index listのエラーに対応するため上下に1行ずつ余分に挿入する
l_img.append(list(".")*(column+2))
l_img.insert(0,list(".")*(column+2))

#引数に渡すリストのインデックスの上下左右を.'にする
def erosion(row,column):
    #上(すでに.が入っていたらpass)
    if l_img[row - 1][column] == ".":
        pass
    #規定値の.と区別するために.'を入力する(最後に.'は.にする)
    else:l_img[row-1][column]=".'"
    #右
    if l_img[row][column+1] == ".":
        pass
    else:l_img[row][column+1] = ".'"
    #左
    if l_img[row ][column-1] == ".":
        pass
    else:l_img[row][column-1] = ".'"
    #下
    if l_img[row + 1][column] == ".":
        pass
    else:l_img[row+1][column] = ".'"
#引数に渡すリストのインデックスの上下左右を#'にする
def dilation(row,column):
    #上(すでに#が入っていたらpass)
    if l_img[row - 1][column] == "#":
        pass
    # 規定値の#と区別するために#'を入力する(最後に#'は#にする)
    else:l_img[row-1][column]="#'"
    #右
    if l_img[row][column+1] == "#":
        pass
    else:l_img[row][column+1] = "#'"
    #左
    if l_img[row][column-1] == "#":
        pass
    else:l_img[row][column-1] = "#'"
    #下
    if l_img[row +1][column] == "#":
        pass
    else:l_img[row+1][column] = "#'"

input_ope=input()
#膨張させるか収縮させるか
l_ope=list(input_ope)
for ope in l_ope:
    if ope=="D":
        for r in range(1,row+1):
            for c in range(1,column+1):
                if l_img[r][c]=="#":
                    dilation(r,c)
        ##'を#に戻す処理
        for r in range(1,row+1):
            for c in range(1,column+1):
                if l_img[r][c]=="#'":
                    l_img[r][c] = "#"
    else :
        for r in range(1,row+1):
            for c in range(1,column+1):
                if l_img[r][c] == ".":
                    erosion(r, c)
        #.'を.に戻す処理
        for r in range(1,row+1):
            for c in range(1,column+1):
                if l_img[r][c]==".'":
                    l_img[r][c] = "."
#2次元リストのl_imgを上下をスライスする。
cut_l_img=l_img[1:-1]

#行列を入れ替える
l_2d_t = [list(x) for x in zip(*cut_l_img)]

#行列を入れ替えた上で上下をスライスする。実質的に左右をスライスしている
cut_l_img2=l_2d_t[1:-1]

#行列を入れ替えて元に戻す。
result= [list(x) for x in zip(*cut_l_img2)]
#2次元リストの要素のみを出力する
for i in range(row):
    print(*result[i],sep="")
