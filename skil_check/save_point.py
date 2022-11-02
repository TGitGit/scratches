import numpy as np
card=input().rstrip().split(" ")
cards=list(map(int,card))
row,column,points=cards

# sheets=np.zeros((row,column))
# for i in range(reserved_num):
#     input_line = input().rstrip().split(" ")
#     reserved= list(map(int, input_line))
#     reserved_row,reserved_column=reserved
#     sheets[reserved_row][reserved_column]=100

# print(sheets)

#ここまで入力。以降処理-------------------------------------------------
#sheetsの配列にマンハッタン距離を入れていく。
# マンハッタン距離とは、ある 2 点 (p, q)、(s, t) に対して、|p - s| + |q - t| で与えられる距離を表します。
#sheets配列の全てのインデックスにマンハッタン距離を足しこんでいく
sheet=[]
N_row=0
N_column=0
m_first=0
m_second=0
for i in range(row):
    line=input()
    line=list(line)
    if "N" in line:
        N_row=i
        N_column=line.index("N")
    sheet.append(line)
save_points=[]
l_manhattah=[]
for r in range(row):
    for c in range(column):
        # print(sheets[r][c])
        #sheets[0][0]から最も良い席までのマンハッタン距離を求める←を全てのインデックスにかける
       if sheet[r][c] == 'N':
           continue
       if sheet[r][c]!="#":
           m_first=N_row-r
        #マイナス値だったら＋に変換

           if m_first<0:
            m_first=-m_first

           m_second=N_column-c
            # マイナス値だったら＋に変換
           if m_second<0:
                m_second=-m_second
           manhattan=m_first+m_second
           l_manhattah.append(manhattan)
           save_points.append(sheet[r][c])
            #全てのインデックスに足しこむ
            # sheets[r][c]=manhattan+sheets[r][c]
adr_dict = dict(zip(save_points,l_manhattah))
# print(sheet)
print(len([i for i, v in enumerate(l_manhattah) if v == min(l_manhattah)]))
# so_l_manhattah=sorted(save_points[:len([i for i, v in enumerate(l_manhattah) if v == min(l_manhattah)])])
# print(so_l_manhattah)
a = sorted(adr_dict.items(), key=lambda i: i[1])
new=(a[:len([i for i, v in enumerate(l_manhattah) if v == min(l_manhattah)])])

sorted_dic = [i[0] for i in new]

print(*sorted_dic,sep="\n")
