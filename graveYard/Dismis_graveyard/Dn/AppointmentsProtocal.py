import subprocess
import os

def appointment():
    ''' Opens 'data/appointments.txt' using gedit to let users to set the appointments manually.
    Also displays the previous appointments. '''

    proc = subprocess.Popen(['gedit', 'data/appointments.txt'])
    proc.wait()

# Looks sloppy! requires refinement


def read_appointment():
    ''' Reads the appointments line by line from appointments.txt '''

    if(os.stat("apple.txt").st_size == 0):
        print("You don't have any appointments.")
    else:
        with open('apple.txt') as f:
            no_of_tasks = sum(1 for _ in f)
            print("You have "+str(no_of_tasks) + " appointments.")
        file = open("apple.txt", "r")
        for line in file:
            print(line)
