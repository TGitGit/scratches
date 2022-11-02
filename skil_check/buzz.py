import pandas as pd
import numpy as np
input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))

voice,hour,time,good=input_line
l=[]
for i in range(hour):
    tw = input().rstrip().split(" ")
    tw = list(map(int, tw))
    l.append(tw)
array=np.array(l)
# array=np.reshape(array,hour,voice)
pd_array=pd.DataFrame(array)
print(pd_array)

for v in range(voice):
    s = []
    for h in range(hour):
        for r in range(time):
            s=pd_array[h:r + h+1].sum()
        if s[v]>=good:
            print("yes "+str(r + h+1))
            break
    else:
        print("no 0")

    # else:break