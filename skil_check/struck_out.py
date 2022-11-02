import itertools

input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))
r,c=input_line
panel=[]
for i in range(r):
    input_line = input()
    panel.append(input_line)
joined_panel="".join(panel)
listed_panel=list(joined_panel)

points=[]
for i in range(r):
    input_line = input().rstrip().split(" ")
    input_line = list(map(int, input_line))
    points.append(input_line)
joined_points=list(itertools.chain.from_iterable(points))

result=0
for i in range(r*c):
    if listed_panel[i]=="o":
        result+=joined_points[i]
print(result)