import time
import sys
import socket
import os
import ctypes
import webbrowser

s = socket.socket()
host = "dismis-slave1"

port = 8080
s.connect((host, port))
print("")
print(" Connected to server ")

command = s.recv(1024)
command = command.decode()
if command == "shutdown":
    print("")
    print("Shutdown command")
    s.send("Command recieved".encode())
    print('Successful controlling Slave')
    os.system("poweroff")
elif command == 'restart':
    print("")
    print("rebooting command")
    s.send("Command recieved".encode())
    print('Successful controlling Slave')
    os.system('reboot')

elif command == 'search':   ##Not working
    print('in google search...')
    s.send("Command recieved".encode())
    print('Successful controlling Slave')
    webbrowser.open('https://www.google.com/search?q={}'.format(command))


elif command == 'open' or command == 'launch':
    print('In open....')
    os.system('explorer C:\\ {}"'.format(command.replace('open ', '').replace('launch', '')))


elif command == 'search':   ##Not working
    print('in google search...')
    webbrowser.open('https://www.google.com/search?q={}'.format(command))

elif command == 'lock':
    for value in ['pc','window','system']:
        ctypes.windll.user32.LockWorkStation()
        print('System locked')



elif command == 'shutdown':
    print('Shuting down')
    try:
        os.system('shutdown -s')
    except:
        os.system('poweroff')

elif command == 'get out':
    print('closing virtual environment in dismis slave one')