"""
ボンバーマン
2次元のマス目を設定し、文字列の"."と"#"で埋める
"#"は爆弾なので縦横全てのマス目を爆発させる。
爆発したマス目を数える

1行目にマス目として行×列を半角数字で半角スペース区切りで入れる。例)5 5
2行目以降に行数分"."か"#"を列数分設定していく(半角スペースはなし)。例)..#..
"""
import numpy as np
import copy

input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))
row,column=input_line

l_input=[]
for i in range(row):
    input_row=input()
    for k in range(column):
        if input_row[k]==".":
            changed_row=0
            l_input.append(changed_row)
        else:
            changed_row=1
            l_input.append(changed_row)

array=np.array(l_input)
array=np.reshape(array,(row,column))
row_array=copy.copy(array)
clumn_array=copy.copy(array)

#numpyにした配列を1行ごとに見る
for j in range(row):
    #axis=1は行を指定。sumして1以上だったら
    if np.sum(row_array,axis=1)[j]>=1:
        # 0を１にしてそうでないものは１のまま
            row_array[j]=np.where(row_array[j]/1==0,1,1)
# print(row_array)
#numpyにした配列を1列ごとに見る
for m in range(column):
    # axis=0は列を指定
    if np.sum(clumn_array,axis=0)[m]>=1:
        # ↓numpyの列を指定
        clumn_array[:,m]=np.where(clumn_array[:,m]/1==0,1,1)
# print(clumn_array)
#処理した配列を足す
total=row_array+clumn_array
print(np.count_nonzero(total>=1))


