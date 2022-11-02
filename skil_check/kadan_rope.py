line = input().rstrip().split(" ")
line = list(map(int, line))
row, column= line

l_kadan=[]

for i in range(row):
    kadan = input()
    kadan = list(map(str, kadan))
    kadan.insert(0,".")
    kadan.append(".")
    l_kadan.append(kadan)

l_kadan.append(list(".")*(column+2))
l_kadan.insert(0,list(".")*(column+2))
lope=0
count=0
for r in range(1,row+1):
    for c in range(1,column+1):

        l=l_kadan[r][c] + l_kadan[r][c + 1] + l_kadan[r + 1][c] + l_kadan[r - 1][c] + l_kadan[r][c - 1]
        s= l.count("#")
        # print(s)
        if l_kadan[r][c]=="#"and s==5:
            pass
        elif l_kadan[r][c]=="#"and s==4:
            lope+=1
        elif l_kadan[r][c]=="#"and s==3:
            lope+=2
        elif l_kadan[r][c]=="#"and s==2:
            lope+=3
        elif l_kadan[r][c]=="#"and s==1:
            lope+=4
        else:pass


print(lope)
            # and l_kadan[i][r+1]=="#" and l_kadan[i+1][r]=="#" and l_kadan[i-1][r] and l_kadan[i][r-1]=="#":
        #     pass
        # elif l_kadan[i][r]=="#"and l_kadan[i][r+1]=="#" and l_kadan[i+1][r]=="#":
        #     lope+=2
        # elif l_kadan[i][r]=="#"and l_kadan[i][r+1]=="#" and l_kadan[i+1][r]=="#":
        #     lope+=2
        # elif l_kadan[i][r]=="#"and l_kadan[i+1][r]=="#":
        #     lope+=3
        # elif l_kadan[i][r] == "#":
        #     lope+=4
        #
