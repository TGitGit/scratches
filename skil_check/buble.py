line = input().rstrip().split(" ")
line = list(map(int, line))
t,x,y = line
l_x=0
l_y=0
l_x += (x)
l_y += (y)
max_l=[]
max_l.append(x)
for i in range(t):
    ido = input().rstrip().split(" ")
    ido = list(map(int, ido))
    x_dis, y_dis = ido
    # l_x += (x_dis)
    # l_y += (y_dis)

    if 0 <= x_dis:
        # max_l=l_x
        # if l_x>=l_x+x_dis:
        #     max_l=l_x

        l_x+=x_dis
        max_l.append(l_x)
    else:
        x_dis=-(x_dis)
        l_x-=x_dis

    l_y+=(y_dis)

    if l_y<=0:
        # maxl = [sum(l_x[0:j]) for j in range(1,len(l_x))]
        print(max(max_l))
        break
else:
    print(max(max_l))
