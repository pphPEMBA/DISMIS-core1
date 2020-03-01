import subprocess

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call)
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())
and now you can do:

>>> process_exists('eclipse.exe')
True

>>> process_exists('AJKGVSJGSCSeclipse.exe')
False





import os

def getTasks(name):
    r = os.popen('tasklist /v').read().strip().split('\n')
    print ('# of tasks is %s' % (len(r)))
    for i in range(len(r)):
        s = r[i]
        if name in r[i]:
            print ('%s in r[i]' %(name))
            return r[i]
    return []

if __name__ == '__main__':
    '''
    This code checks tasklist, and will print the status of a code
    '''

    imgName = '/home/pemba/Dismis-HA_GUI/test.py'

    notResponding = 'Not Responding'

    r = getTasks(imgName)

    if not r:
        print('%s - No such process' % (imgName)) 

    elif 'Not Responding' in r:
        print('%s is Not responding' % (imgName))
        
    else:
        print('%s is Running or Unknown' % (imgName))










