from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")# 가로 * 세로

txt= Text(root, width=30,height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)# 엔터를 입력 할 수 없다
e.pack()
e.insert(0, "한줄만 입력해요")

def btncmd():
    #내용 추가
    print(txt.get("1.0", END))# 1줄에서 0번쨰 인덱스에서 가져와라
    print(e.get())
    
    # 내용삭제
    txt.delete("1.0", END)
    e.delete(0, END)
# 1: 첫번쨰 라인, 0: 0번쨰 colum위치
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()
