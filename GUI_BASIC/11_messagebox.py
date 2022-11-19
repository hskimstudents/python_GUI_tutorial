import tkinter
import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
# root.iconphoto(False,tkinter.PhotoImage(file=''))
# icon=tkinter.PhotoImage(file='icon.png')
# root.wm_iconphoto(False, icon)
# root.iconbitmap("icon.png")
root.title("기차예매 시스템")
root.geometry("640x480")# 가로 * 세로

# 기차 예매 시스템이라고 가정
def info():
    msgbox.showinfo("알림","정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고","해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("에러","결제 오류가 발생하였습니다.")
    
def okcancer():
    msgbox.askokcancel("확인/취소","해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")

def yesno():
    msgbox.askyesno("예/ 아니요","해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response =msgbox.askyesnocancel(title=None,message=" 예매 내역이 저장되지 않았습니다.\n저장 후 프로그램을 종료하시겠습니까?")
    # 네 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소 (현재 화면에서 계속 작업)
    print("응답 : ", response) # True, False, None --> 예 1 아니오 0 , 그외
    if response == 1:
        print("예")
        msgbox.showinfo("예","저장 후 종료하였습니다.")
    elif response == 0:
        print("아니오")
        msgbox.showinfo("아니오","저장 하지 않고 종료 하였습니다.")
    else:
        print("취소")
        msgbox.showinfo("취소", "프로그램 종료 취소하였습니다.")



def Close():
    root.destroy()

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancer, text="확인/ 취소").pack()
Button(root, command=retrycancel,text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()
Button(root, command=Close, text="나가기").pack()#1
# Button(root, command=root.destroy, text="나가기").pack()#2


root.mainloop()
