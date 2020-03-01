#List all the file from it	

import glob, os;
directory = input("Enter directory to list all files it contains: ");
os.chdir(directory);
for file in glob.glob("*.*"):
    print(file);
 
import glob, os

def extension_txt():
    currentDirectory = os.getcwd()
    for file in glob.glob("*.txt"):
        print(file)

def extension_pdf():
    currentDirectory = os.getcwd()
    for file in glob.glob("*.pdf"):
        print(file)

def extension_mp4():
    currentDirectory = os.getcwd()
    for file in glob.glob("*.mp4"):
        print(file)

def extension_docx():
    currentDirectory = os.getcwd()
    for file in glob.glob("*.docx"):
        print(file)

def extension_mp3():
    currentDirectory = os.getcwd()
    for file in glob.glob("*.mp3"):
        print(file)
