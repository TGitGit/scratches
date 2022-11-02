input_line=int(input())
dic={}
for i in range(input_line):
    line = input().rstrip().split(" ")
    # line = list(map(int, line))
    a = line[0]
    num = int(line[1])
    if a in dic.keys():
        dic[a]+=num
    else:dic[a]=num
# print(dic)

dic_sorted = sorted(dic.items(), key=lambda x:x[1],reverse=True)
# dic2_value=[dic_sorted[i][1] for i in range(input_line)]
for i in dic_sorted:
    print(*i)
