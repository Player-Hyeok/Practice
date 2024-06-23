# 모든 프로그램은 주석 처리되어 있음. """을 없애면 실행됨.

# 1. 업다운 게임 (1~100 사이 숫자 맞추기)
""" import random

number = random.randint(1, 100) # 랜덤 수 정하기
count = 0 # 도전 횟수

while True:
    answer = int(input('내가 고른 숫자를 맞혀 봐! : '))
    count += 1
    if answer == number:
        print('제법이군! 정답이야!')
        print(str(count)+'번 만에 정답을 맞췄어!')
        break
    elif answer < number:
        print('업 Up!')
    else:
        print('다운 Down!') """
        
        
# 2. turtle 라이브러리를 사용해 미술 작품을 만들어 보자.
# t.shape(classic / turtle / arrow / squarte / triangle / circle )

import turtle as t
import random
'''
t.speed(0)
t.shape('turtle')
t.bgcolor('black')
colors = ['orange', 'skyblue', 'yellow']

i=0
while True:
    t.color(colors[i % 3])
    t.fd(i)   # fd 는 앞으로 이동
    t.lt(119) # lt 는 왼쪽으로 회전
    i += 1
'''
'''
#turtle graphics 2
t.speed(0)
t.shape('turtle') 
t.bgcolor('black')
colors = ['deeppink', 'orange', 'gold', 'greenyellow', 'deepskyblue', 'magenta']

for i in range (300):
    t.penup()
    
    x=random.randint(-400, 400)
    y=random.randint(-400, 400)
    t.goto(x,y)
    
    c= random.choices(colors)
    t.color(c)
    
    t.pendown()
    draw = random.choice([t.circle, t.dot])
    size = random.randint(1, 100)
    draw(size)
'''
# 3. turtle 그림판 만들기 - 키보드 조작 가능
# function 파일 생성
'''
def go_right():
    t.setheading(0) #turtle 머리를 0도로 지정
    t.fd(10)
    
def go_up():
    t.setheading(90)
    t.fd(10)
    
def go_left():
    t.setheading(180)
    t.fd(10)
    
def go_right():
    t.setheading(270)
    t.fd(10)'''

#소스 코드
'''
from basic_program_function import *
import turtle as t

t.shape('turtle')
t.onkeypress(go_right, 'Right')  #함수와 방향키 연결
t.onkeypress(go_left, 'Left')  #함수와 방향키 연결
t.onkeypress(go_up, 'Up')  #함수와 방향키 연결
t.onkeypress(go_down, 'Down')  #함수와 방향키 연결

t.onkeypress(pen_updown, 'Return')  # enter 키로 펜 들고 안들고(선 없게 나옴)
t.onkeypress(change_color, 'c') # c 키는 색 변경
t.onkeypress(clear, 'Escape') # escape 는 종료

# 터틀 화면이 키보드의 입력 데이터를 계속 관찰하고 처리하는 코드
t.listen()
t.mainloop()
'''

# 4. 디지털 시계 만들기
import tkinter as tk  # 창 화면과 버튼을 만들게 해주는 라이브러리
import time

def clock():
    now = time.strftime("%Y/ %m/ %d/ \n %H:%M:%S")
    label.configure(text=now)
    label.after(1000, clock)

window = tk.Tk()
window.title("디지털시계")
window.geometry('400x300')

font = ('맑은 고딕', 25, 'bold')
label = tk.Label(text = '시작 버튼을 누르세요', font=font)
button = tk.Button(text='시작', font=font, width=4, height=1, command=clock)
label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

window.mainloop()

