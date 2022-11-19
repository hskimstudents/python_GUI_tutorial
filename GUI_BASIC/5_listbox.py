from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")# 가로 * 세로

listbox = Listbox(root,selectmode="extended", height=0) # 높이는 개수만 보여줌 0 일경우 리스트가 포함하는 개수만큼만 보여줌

listbox.insert(0,"사과")
listbox.insert(1,"strawberry")
listbox.insert(2,"banana")
listbox.insert(3, "watermelon")
listbox.insert(END,"grape")
listbox.pack()


def btncmd():
    # pass
    # listbox.delete(END)# 맨 뒤에 항목을 삭제
    # listbox.delete(0) # 0번쨰 리스트 값 삭제


    #갯수 확인
    # print("리스트에는", listbox.size(),"개가 있어요")
    
    #항목 확인 (start index, end index)
    # print("1번쨰부터 3번째까지의 항목 :", listbox.get(0,2))
    
    # 선택된 항목 확인 
    print("selected value :", listbox.curselection())
    
btn = Button(root,text="클릭", command=btncmd)
btn.pack()

root.mainloop()
