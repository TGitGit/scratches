input_meirei=int(input())
default_kabu=input().rstrip().split(" ")
default_kabu=list(map(int,default_kabu))
# print(default_kabu)
s=[]
for i in range(input_meirei):
   o =input().rstrip().split("\r\n")
   s.append(o)

class red_kabu:
    def __init__(self):
        self.kabu=default_kabu[0]
    def right_move(self,R):
        if "R R"in R or "R Y"in R or"R M"in R or  "R W"in R:
            self.kabu+=1
            print("赤カブが右に１つ進みました")
        else:
            print("何もしません")

    def left_move(self, L):
        if "L R"in L or "L Y"in L or "L M"in L or"L W"in L:
            self.kabu -= 1
            print("赤カブが左に１つ進みました")
        else:
            print("何もしません")


class green_kabu:
    def __init__(self):
        self.kabu=default_kabu[1]
    def right_move(self,R):
        if "R G"in R or "R Y"in R or "R C"in R or "R W"in R :
            self.kabu+=1
            print("緑カブが右に１つ進みました")
        else:
            print("何もしません")

    def left_move(self, L):
        if "L G"in L or "L Y"in L or "L C"in L or "L W"in L :
            self.kabu -= 1
            print("緑カブが左に１つ進みました")
        else:
            print("何もしません")

class blue_kabu:
    def __init__(self):
        self.kabu=default_kabu[2]
    def right_move(self,R):
        if "R B"in R or "R M"in R or "R C"in R or "R W"in R:
            self.kabu+=1
            print("青カブが右に１つ進みました")
        else:
            print("何もしません")

    def left_move(self, L):
        if "L B"in L or "L M"in L or "L C"in L or "L W"in L:
            self.kabu -=1
            print("青カブが左に１つ進みました")
        else:
            print("何もしません")


red_kab=red_kabu()
green_kab=green_kabu()
blue_kab=blue_kabu()
for order in range(input_meirei):
    print(s[order])
    red_kab.right_move(s[order][0])
    red_kab.left_move(s[order][0])
    green_kab.right_move(s[order][0])
    green_kab.left_move(s[order][0])
    blue_kab.right_move(s[order][0])
    blue_kab.left_move(s[order][0])

    # print(red_kab.kabu)
    # print(green_kab.kabu)
    # print(blue_kab.kabu)
    if red_kab.kabu is green_kab.kabu is blue_kab.kabu:
        print (str(order+1)+"回目で一致")
        break

else:print("no")



# for r in range(s)

# for i in range(input_meirei):
#     red_kab.right_move()
