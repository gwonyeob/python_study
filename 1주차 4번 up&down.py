from random import *
answer = int(randint(1, 100))

while True:
    try:
        x = int(input('숫자를 예측해보세요(1~100)>> '))
        if answer == x:
            print('정답입니다!')
            break
        elif answer > x:
            print('숫자가 높습니다')
        else:
            print('숫자가 낮습니다')
    except:
        print("숫자를 에측해보세요(1~100)>>")
