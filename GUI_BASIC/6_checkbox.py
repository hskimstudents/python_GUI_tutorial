from msilib.schema import CheckBox
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")# 가로 * 세로

chkvar = IntVar() # chkvar 에 int 형으로 값을 저장한다
chkbox = Checkbutton(root, text="오늘 하루 보지않기", variable=chkvar)

# chkbox.select()# 자동 선택 처리
# chkbox.deselect() # 선택 해제 처리

chkbox.pack()

chkvar2=IntVar()
chkbox2= Checkbutton(root, text="일주일동안 보지않기",variable=chkvar2)
chkbox2.pack()



def btncmd():
    print(chkvar.get())
    print(chkvar2.get())
    
  
btn = Button(root,text="클릭", command=btncmd)
btn.pack()

root.mainloop()
