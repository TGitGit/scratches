price=input().rstrip().split(" ")
price=list(map(int,price))
cameras,over_speed=price

sppeds=[]
came=[]
for i in range(cameras):
    price = input().rstrip().split(" ")
    price = list(map(int, price))
    camera, speed = price
    sppeds.append(speed)
    came.append(camera)
# flag=False
adr_dict = dict(zip(came,sppeds))
stop=0
r = 1
flag=False
for i in range(len(came)):
    if stop==len(came)-1:
        break

    # if sppeds[0]/came[0]>over_speed:
    #     print("YES")
    #     flag = True
    #     break

    if (sppeds[r]-sppeds[r-1])/(came[i+1]-came[i])>over_speed:
            print("YES")
            flag=True
            break
    r+=1
    stop+=1
if not flag:
    print("NO")

# stop=0
# r=1
# for i in adr_dict:
#     if stop==len(came)-1:
#         break
#     if (adr_dict[i]-adr_dict[i])/(came[r])-came[r-1]>over_speed:
#         print("YES")
#         break
#
#     stop+=1