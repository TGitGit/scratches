line = input().rstrip().split(" ")
shops,month = list(map(int, line))

line = input().rstrip().split(" ")
shop_cost,human_cost,one_profit = list(map(int, line))
uriage=[]
for shop in range(shops):
    uriage.append(int(input()))
minus=0
for shop in range(shops):
    if one_profit*uriage[shop]-shop_cost-(human_cost*month)<0:
        minus+=1
print(minus)