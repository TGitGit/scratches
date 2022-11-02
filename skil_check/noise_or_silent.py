line = input().rstrip().split(" ")
line = list(map(int, line))
a,b,r = line

tree_n = int(input())

for i in range(tree_n):
    tree = input().rstrip().split(" ")
    tree = list(map(int, tree))
    x1, y1= tree
    if (x1-a)**2+(y1-b)**2>=r**2:
        print("silent")
    else:
        print("noisy")