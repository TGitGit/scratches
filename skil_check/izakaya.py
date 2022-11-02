
class Customer:
    def __init__(self,old):
        self.old=old
        self.price=0
        self.flag = False
    def order_alc(self,price):
        pass
    def order_food(self, price):
        if self.flag:
            price=price-200
        self.price += price
    def get_price(self):
        return self.price

class Adult(Customer):

    def __init__(self, old):
        super().__init__(old)

    def order_alc(self,price):
        self.price+=price
        self.flag=True

input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))
cust_num,count_order=input_line
l_cust=[]
for i in range(cust_num):
    old = int(input())
    if old >=20:
        l_cust.append(Adult(old))
    else:
        l_cust.append(Customer(old))

for i in range(count_order):
    order=input().rstrip().split(" ")
    num=int(order[0])
    order_type=order[1]
    pay=int(order[2])

    if order_type=="alcohol":
        l_cust[num - 1].order_alc(pay)
    elif order_type=="food":
        l_cust[num - 1].order_food(pay)
    elif order_type=="softdrink":
        l_cust[num - 1].order_food(pay)

for cus in l_cust:
    print(cus.get_price())