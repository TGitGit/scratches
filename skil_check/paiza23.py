input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))
human,present_1,present_2=input_line
i=1
for i in range(1,human+1):
    if i%present_1==0 and i%present_2==0:
        print("AB")
    elif i%present_2==0:
        print("B")
    elif i%present_1==0:
        print("A")
    else:
        print("N")

