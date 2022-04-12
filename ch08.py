import random       #랜덤 모듈을 가져옴
import time         #시간 관련 모듈을 가져옴

correctAns = 0      #맞은 개수
wrongAns = 0        #틀린 개수

count = int(input("몇번할까요?"))
while (count != 0):
    a = random.randint(3, 9)        #3단부터 9단까지 숫자 생
    b = random.randint(3, 9)

    if ((a == 5) or (b == 5)):      #5단이면 다시 난수 받기
        continue

    count = count - 1
    print("%d x %d?" %(a, b))
    startTime = time.time()
    product = int(input(">>>"))      #반응 시간을 측정
    endTime = time.time()
    print("%.1f 초만에 답을 했어요" %(endTime - startTime))

    #곱셈이 맞았는지 점검하고 시간 초과도 검사함
    if((product == a * b) and ((endTime - startTime) <= 3)): 
        correctAns = correctAns + 1                          
        print("맞았습니다!")
    else:
        wrongAns = wrongAns + 1
        print("다시 도전해 보세요")

#전체 맞힌 개수를 알려줌
print("%d번 중 %d번 맞았어요" %((correctAns + wrongAns), correctAns))
        
