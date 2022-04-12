import random       #난수 모듈을 불러옴

guessNumber = -1    #초기 숫자 설정(초기화)
playAgain = 'YES'   #게임 반복 상태 설정

print("반갑습니다. UP&DOWN게임을 시작하겠습니다.")
print("1부터 30까지의 숫자를 맞춰야 합니다.")

while(playAgain == 'YES'):
    count = 1
    ansNumber = random.randint(1, 30)
    while(count <= 5):      #제한 횟수 5번
        guessNumber = int(input("추측한 숫자를 입력하세요>>>"))
        if(guessNumber == ansNumber):   #정답을 맞추면 while문을 빠져나
            print("정답입니다!")
            break
        elif(guessNumber < ansNumber):
            print("추측한 숫자보다 큽니다. 남은기회", 5 - count)
        else:
            print("추측한 숫자보다 작습니다. 남은기회", 5 - count)
        count += 1          #시도 횟수 카운트

    if(count > 5):          #시도횟수가 초과되면 실패
        print("오답입니다! 정답은", ansNumber, "입니다.")

    playAgain = input("재도전?(YES or NO)")
