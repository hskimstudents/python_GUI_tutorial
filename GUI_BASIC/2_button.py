from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1= Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")# 버튼 글자 위 옆으로 간격을 설정
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # 버튼 자체 크기를 설정
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", width=10, height=3, text="버튼 5")
btn5.pack()

photo = PhotoImage(file="img.png")
btn6=Button(root,image=photo)
btn6.pack()
def btncmd():
    print("버튼이 동작되었어요")
btn7= Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack() # 이런식으로 동작 삽입 가능


root.mainloop()
