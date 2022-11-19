# QUize) tkinter 를 이용한 메모장 만들기

# [GUI Condition]
# 1. title: 제목 없음 - windows 메모장
# 2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
# 3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
# 3-1. 열기 :mynote.txt 파일 내용 열어서 보여주기
# 3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
# 3-3. 끝내기 : 프로그램 종료
# 4.프로그램 시작은 항상 비어있는 상태
# 5. 하단의 status 바는 필요 없음
# 6. 프로그램 크기, 위치는 자유롭게 하되 크기 조절 가능해야 함
# 7. 본문 우측에 상하 스크롤 바 넣기

from tkinter import *

root = Tk()
root.title("제목 없음 - windows 메모장")
root.geometry("640x480")
menu = Menu(root)
#파일 메뉴
def open_file():
    print("테스트중..")
    open("mynote.txt",'w')

def save_file():
    print("테스트중..")

menu_file= Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command= save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일(F)",menu=menu_file)

# 편집 메뉴
menu_editor=Menu(menu, tearoff=0)
menu.add_cascade(label="편집(E)",menu=menu_editor)

#서식
menu_format=Menu(menu, tearoff=0)
menu.add_cascade(label="서식(O)", menu=menu_format)
#보기
menu_view=Menu(menu, tearoff=0)
menu.add_cascade(label="보기(V)",menu=menu_view)
#도움말
menu_help=Menu(menu,tearoff=0)
menu.add_cascade(label="도움말",menu=menu_help)

txt= Text(root)
txt.pack(side=LEFT,expand=True,fill="both")
# txt.grid(row=0,column=0,columnspan=2, sticky=N+E+S+W)

root.config(menu=menu)
root.mainloop()