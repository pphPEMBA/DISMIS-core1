""" running in ~/.profile """
import psutil
import os
import time

class checkProcessRunning:
    def is_running(script):
        for q in psutil.process_iter():
            if q.name().startswith('python3'):
                if len(q.cmdline())>1 and script in q.cmdline()[1] and q.pid !=os.getpid():
                    print("'{}' Process is already running".format(script))
                    return True
        return False
    def check_Is_running():
        if not checkProcessRunning.is_running("/home/d-slave1/.Dismis-HA_slave1/DISMIS-HA.py"):
            print('Dismis-HA_slave1 is not running')
            from gi.repository import Notify
            # One time initialization of libnotify
            Notify.init("Dismis-HA_slave1")
            # Create the notification object
            title = "Dismis-HA_slave1!"
            body = "Dismis-HA_slave1 has stopped"
            notification = Notify.Notification.new(
                title, body)
            # Actually show on screen
            notification.show()
            
while True:
    time.sleep(5)
    checkProcessRunning.check_Is_running() #check in the interval of 2 minutes 5 seconds.
    time.sleep(600)
