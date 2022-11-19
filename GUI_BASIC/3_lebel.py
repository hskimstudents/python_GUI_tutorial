from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

label1= Label(root, text="안녕하세요")
label1.pack()

photo=PhotoImage(file="img.png")
label2= Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")
    
    global photo2 # 안해주면 지역변수로써 garbage collecter가 photo2를 삭제 할 수 있음..
    photo2 = PhotoImage(file="img2.png")
    label2.config(image=photo2)
    
    

btn = Button(root, text="클릭", command=change)
btn.pack()
root.mainloop()
