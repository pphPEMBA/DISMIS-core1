import time
from datetime import datetime


while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    if current_time == "10:59:00":
        print & ("alarm", "this is the message")
        break
    else:
        pass


