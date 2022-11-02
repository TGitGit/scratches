class Customer:
    def __init__(self):
        self.sum = 0

    def take_food(self, price):
        self.sum += price

    def take_softdrink(self, price):
        self.sum += price

    def take_alcohol(self, price=500):
        # 何もしない (却下)
        pass

    def get_sum(self):
        return self.sum


class Adult(Customer):
    def __init__(self):
        super().__init__()
        self.alcohol = False

    def take_food(self, price):
        if self.alcohol:
            self.sum += price - 200
        else:
            self.sum += price

    def take_alcohol(self, price=500):
        self.sum += price
        self.alcohol = True


n, k = [int(x) for x in input().split()]

customers = [None] * n
for i in range(n):
    age = int(input())

    if age >= 20:
        customers[i] = Adult()
    else:
        customers[i] = Customer()
out=0
for _ in range(k):
    values = input().split()

    index = int(values[0]) - 1
    order = values[1]
    if order=="A":
        print(customers[index].get_sum())
        out+=1
    elif order == "0":
        customers[index].take_alcohol()
    else:
        price = int(values[2])

        if order == "food":
            customers[index].take_food(price)
        elif order == "softdrink":
            customers[index].take_softdrink(price)
        else:
            customers[index].take_alcohol(price)
print(out)
#
# for _ in range(k):
#     if customer=="A":
#         print(customer.get_sum())