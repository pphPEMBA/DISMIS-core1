def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    
DisError = 'System Failure! Unable to perform googleCalender skill sir'
print('****************************************************************')
print(' ')
Log_Time()
print('***System Failure! Unable to get current time sir***')
print('***' + DisError + '***')
print(' ')
print('****************************************************************')