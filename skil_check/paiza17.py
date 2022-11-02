import numpy as np

input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))
# n=np.arange(input_line[0],input_line[0])
# n=np.empty((input_line[0],input_line[0]),int)
root=[]
for i,l in enumerate(range(input_line[0])):
    row=input().rstrip().split(" ")
    row = list(map(int, row))
    root.append(row)

#     n=np.append(n,np.array(list(row)),axis=0)
array=np.array(root)
print(array)
colums=np.max(array,axis=0)
print(colums)
wait_count=0
lis=[]
for  i in range(input_line[0]):
    if colums[i]<input_line[1]:
        # print((i+1), end=' ')
        lis.append(i+1)

        wait_count+=1
print(*lis)
if wait_count==0:
    print("wait")