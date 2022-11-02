class solution():

    def elevator(self,n):
        s = []
        s.append(1)
        step=[]
        for idou in range(0,n):
            log=int(input())

            s.append(log)
            if log-s[idou]>0:
                step.append(log - s[idou])
            else:
                step.append(-(log-s[idou]))

        print("止まった階"+str(s))
        print("移動数"+str(step))
        print("合計移動数"+str(sum(step)))
        # for i in range(1,n):
        #
        #     step[i]-
        # print(step)









solution().elevator(3)