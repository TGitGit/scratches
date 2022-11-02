t = input().rstrip().split(" ")

m=int(t[0])
p=m*float(t[1])*0.01

osouzai=m-p


q=osouzai*float(t[2])*0.01
print(osouzai-q)
