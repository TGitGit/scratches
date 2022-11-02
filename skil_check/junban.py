input_line = input()
string=list(input_line)
old=string[0]+string[-1]

new=sorted(string[0]+string[-1])
new=new[0]+new[1]
if old==new:
    print("true")
else:print("false")