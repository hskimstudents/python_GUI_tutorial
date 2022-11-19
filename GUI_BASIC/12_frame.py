from tkinter import *

root = Tk()
# root.iconphoto(False,tkinter.PhotoImage(file=''))
# icon=tkinter.PhotoImage(file='icon.png')
# root.wm_iconphoto(False, icon)
# root.iconbitmap("icon.png")
root.title("Nado GUI")
root.geometry("640x480")# 가로 * 세로

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

frame_burger =Frame(root ,relief="solid", bd=1)
frame_burger.pack(side="left",fill="both", expand=True)

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()


frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right",fill="both", expand=True)

Button(frame_drink, text="cola").pack()
Button(frame_drink, text="soda").pack()
Button(frame_drink, text="juice").pack()


root.mainloop()
