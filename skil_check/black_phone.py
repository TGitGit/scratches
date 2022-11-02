input_line=input().rstrip().split("-")
dis=list(map(str,input_line))
one,twp,three=dis
l=0
for i in range(len(one)):
    num=str(one)[i:i+1]
    # num=int(num)
    if num=="0":
        l+=12*2
    else:l+=(int(num)+2)*2

for i in range(len(str(twp))):
    num=str(twp)[i:i+1]
    # num = int(num)
    if num=="0":
        l+=12*2
    else:l+=(int(num)+2)*2

for i in range(len(str(three))):
    num = str(three)[i:i + 1]
    # num = int(num)
    if num == "0":
        l += 12*2
    else:l += (int(num) + 2) * 2

print(l)