input_line=int(input())
dic={}
dic2={}
for i in range(input_line):
    line=input().rstrip().split(" ")
    string,num=line
    num=int(num)
    dic[num]=string
dic2=sorted(dic.items())

dic2_value=[dic2[i][1] for i in range(input_line)]
print(*dic2_value,sep="\n")
