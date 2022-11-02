line=int(input())
char_num=[]
zero=0
l=list([5,1,1,1,10])

# s=sorted(l)

for num in l:
    # if num ==min(l):
    #     l.insert(0,num)
    #     del l[num+1]

    char_num.append(input())
int_char=list(map(int,char_num))
sor_cha=sorted(int_char)
char_num.sort()
dic_sor=dict(zip(char_num,sor_cha))
print(sor_cha)
print (char_num)
