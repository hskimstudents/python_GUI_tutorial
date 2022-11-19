
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")# 가로 * 세로

#---------------------------
# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # mode 값: indeterminate ==> 결정되지않아서 언제 끝날지 모름
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) # 10 ms 마다 움직임
# progressbar.pack()



# def btncmd():
#     progressbar.stop()
    

# btn = Button(root,text="중지", command=btncmd)
# btn.pack()
#------------------------

import time

p_var2= DoubleVar()
progressbar2= ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1~100
        time.sleep(0.01)  # wait for 0.01s
        
        p_var2.set(i) #prgress bar 의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get()) 
        

btn = Button(root,text="start", command=btncmd2)
btn.pack()
root.mainloop()
