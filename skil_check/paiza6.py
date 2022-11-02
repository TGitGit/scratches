class solution():
    def happy_day(self):
        day=[]
        m=int(input())
        for i in range (1,366):
            if str(m) in str(i):

                day.append(i)
        print(len(day))

solution().happy_day()