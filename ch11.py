value = 0
while True:
    print("\n현재 값 : ", value)
    line = input("작업 명령 입력 :  ")
    tokens = line.split()
    if len(tokens) > 0:
        operator = tokens[0]
        if len(tokens) == 1:
            if operator == 'x':
                break
            print("잘못된 작업 명령!!")
        elif len(tokens) == 2:
            operand = float(tokens[1])
            if operator == '=':
                value = operand
            elif operator == '+':
                value += operand
            elif operator == '-':
                value -= operand
            elif operator == '*':
                value *= operand
            elif operator == '/' or operator == '%':
                if operand != 0:
                    if operator == '/':
                        value /= operand
                    else:
                        value %= operand
                else:
                    print("잘못된 작업 명령(0으로 나누기)!!")
            else:
                print("잘못된 작업 명령!!")
        else:
            print("잘못된 작업 명령!!")
