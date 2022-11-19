from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100")

frame=Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right",fill="y")

listbox = Listbox(frame,selectmode="extended",height=10, yscrollcommand= scrollbar.set)

# set 이 없으면 스크롤 내려고 다시 내려옴

for i in range(1,32):
    listbox.insert(END,str(i)+"일")

scrollbar.config(command=listbox.yview)

listbox.pack()
root.mainloop()
