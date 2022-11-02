# from datetime import datetime,time,timedelta
# minute = 73
# if minute >= 60:
#     hour,min = divmod(minute,60)
#     result = time(hour,min)
#     print(result)
import math
input_line=input().rstrip().split(" ")
left,right=input_line
month,day=input_line[0].split("/")
hour,minute=input_line[1].split(":")
# month,day,hour,minute=int(month,day,hour,minute)
# print(month,day,hour,minute)
append_day=int(hour)/24
new_day=int(day)+append_day

append_hour=int(hour)%24
append_hour=str(append_hour)
# new_hour=int(hour)+append_hour
print(month+"/"+str(math.floor(new_day))+" "+append_hour.zfill(2)+":"+minute)
