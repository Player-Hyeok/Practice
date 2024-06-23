# 1. 업다운 게임 (1~100 사이 숫자 맞추기)
import random

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
        print('다운 Down!')
        


