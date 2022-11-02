
input_line=input().rstrip().split(" ")
l=[]
x=0
a=0
b=0
c=0
flag=False

try:
    a=int(input_line[0])
except:
    flag=True
    pass

if input_line[2]=="x":
    pass
else:
    b=input_line[1]+input_line[2]
    b=int(b)

try:
    c=int(input_line[-1])
except:
    pass

x=(-a + (-b) + c)
if not flag:
    x=-x
print(x)