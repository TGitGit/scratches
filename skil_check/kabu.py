input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))
days,low,high=input_line
total_kabu=0
rieki=0
for i in range(days):
    kabu = int(input())
    if i == days-1:
        kabu=kabu*total_kabu
        rieki += kabu
    elif kabu<=low:
        total_kabu+=1
        kabu=-(kabu)
        rieki+=kabu
    elif kabu>=high:
        kabu=kabu*total_kabu
        total_kabu=0
        rieki += kabu
    else:
        pass
print(rieki)