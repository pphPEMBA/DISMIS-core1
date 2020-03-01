from datetime import datetime

now = datetime.now()
now.strftime()
start_time = now.strftime("%H","%M","%S")
if int(start_time.split(":")[0]) < 12:
    start_time = start_time + " am"
else:
    start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
    start_time = start_time + " pm"
print('today date' , start_time)