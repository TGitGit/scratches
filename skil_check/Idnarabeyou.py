ready=int(input())
l=[]
indexs=[]
name=[]
for i in range(ready):
     strings=input()
     l=list(strings)
     # print(l)
     name.append(strings)

     for index,r in enumerate(l):
         # if not flag:
         try:
            if int(r):
               pass
         except:continue

         indexs.append(strings[index:])
         break
indexs = list(map(int, indexs))
#listとlistを合体させて辞書型にする
adr_dict = dict(zip(indexs,name))
#キーと値をタプルのリストで一覧で得る
sorted_dic=list(sorted(adr_dict.items()))
#内包表記　タプルの2番目の要素のみつまり値のみを抜き出す。
sorted_dic = [i[1] for i in sorted_dic]
print(*sorted_dic,sep="\n")

