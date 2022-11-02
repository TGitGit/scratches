goods=int(input())

price=input().rstrip().split(" ")
price=list(map(int,price))
# a,b,c=price

money=input().rstrip().split(" ")
money=list(map(int,money))
money,order=money

for i in range(order):
    line = input().rstrip().split(" ")
    line = list(map(int, line))
    order_goods, buy = line
    if money-(price[order_goods-1]*buy)>=0:
        money=money - (price[order_goods-1] * buy)
print(money)