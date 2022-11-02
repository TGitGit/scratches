"""
https://paiza.jp/works/challenges/533/retry
映画館の席の予約
入力例1
9 4 5 2 3
1 0
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
出力例1
0 3
2 1
3 2

"""
import numpy as np
#1 行目にすでに予約されている座席の数 N、映画館の座席の縦の数 H、映画館の座席の横の数 W、最も見やすい席の p 座標、q 座標を表す P, Q がそれぞれ半角スペース区切りで与えられます。
input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))
reserved_num,row,column,p,q=input_line
print(input_line)
#np.zerosで0値の入ったnumpy配列を作成し席に見立てる。タプルなので(())二重カッコらしい
sheets=np.zeros((row,column))
#入力された予約されている席のインデックスに値として100を足しこむ
for i in range(reserved_num):
    input_line = input().rstrip().split(" ")
    reserved= list(map(int, input_line))
    reserved_row,reserved_column=reserved
    sheets[reserved_row][reserved_column]=100

print(sheets)

#ここまで入力。以降処理-------------------------------------------------
#sheetsの配列にマンハッタン距離を入れていく。
# マンハッタン距離とは、ある 2 点 (p, q)、(s, t) に対して、|p - s| + |q - t| で与えられる距離を表します。
#sheets配列の全てのインデックスにマンハッタン距離を足しこんでいく
for c in range(column):
    for r in range(row):
        print(sheets[r][c])
        #sheets[0][0]から最も良い席までのマンハッタン距離を求める←を全てのインデックスにかける
        m_first=p-r
        #マイナス値だったら＋に変換
        if m_first<0:
            m_first=-m_first

        m_second=q-c
        # マイナス値だったら＋に変換
        if m_second<0:
            m_second=-m_second
        manhattan=m_first+m_second
        #全てのインデックスに足しこむ
        sheets[r][c]=manhattan+sheets[r][c]
print(sheets)
#ここまで処理。以降出力------------------------------------------
#最小値（一番良い席から一番近い席）があるインデックスを全て抽出
minIndex = np.where(sheets == sheets.min())
for i in range(len(minIndex[0])):
    print(minIndex[0][i],end=" ")
    print(minIndex[1][i])