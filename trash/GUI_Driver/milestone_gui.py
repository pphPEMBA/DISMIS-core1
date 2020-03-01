#from tkinter import *



milestone_txt = open('milestone.txt','r')
result = milestone_txt.read()

root = Tk()
root.geometry('1150x300+120+0')
root.title("Dismis's Conversation")
Label(root, padx=3000, pady=3000, compound=CENTER,
                text=result, bg="#171717", fg="white", font='times 15 bold').pack()
root.after(2800, lambda: root.destroy())
root.mainloop()