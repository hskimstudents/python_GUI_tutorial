from msilib.schema import CheckBox
from tkinter import *
from tokenize import String

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")# 가로 * 세로

Label(root,text="메뉴를 선택해주세요").pack()

burger_val=IntVar()
btn_burger1=Radiobutton(root, text="deri-burger",value=1, variable=burger_val)
btn_burger1.select()
btn_burger2=Radiobutton(root, text="chicken-burger",value=2, variable=burger_val)
btn_burger3=Radiobutton(root, text="double-bulgogi-burger",value=3, variable=burger_val)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 주문해주세요!").pack()

drink_val= StringVar()
btn_drink1=Radiobutton(root, text="soda", value="soda", variable=drink_val)
btn_drink1.select()
btn_drink2=Radiobutton(root, text="cola", value="cola", variable=drink_val)
btn_drink3=Radiobutton(root, text="hwanta", value="hwanta", variable=drink_val)
btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()
def btncmd():
    ham_burger=""
    ind=burger_val.get()
    if ind==1:
        ham_burger="dari-burger"
    elif ind==2:
        ham_burger="chicken-burger"
    elif ind==3:
        ham_burger="double-bulgogi-burger"
    print("ham-burger_is_"+ham_burger)
    print("drink_is_"+drink_val.get())
  
btn = Button(root,text="ORDER", command=btncmd)
btn.pack()

root.mainloop()
