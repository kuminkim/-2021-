print('====================================================================')
print('==                       당신들을 도둑입니다.                     ==')
print('====================================================================')

print()
print('====================================================================')
print('==   경찰에게 잡히기 전에 암호를 풀어 보물의 위치를 알아내세요.   ==')
print('==             1부터 15까지의 숫자만 고를 수 있습니다.            ==')
print('==               단, 5개의 힌트를 볼 수 있습니다.                 ==')
print('==                 원하시는 번호를 입력하세요.                    ==')
print('==           신중하게 선택하시는 것이 좋을 것 입니다.             ==')
print('====================================================================')


for a in range(1,6,1):
    print()
    num = int(input('원하시는 번호를 입력하세요 : '))

    a = 0
    if num==1 :
        print('난 이걸 들으면 외국이 생각나')
    elif num==2 :
        print('난 이거하면 떠오르는 한사람이 있어')
    elif num==3 :
        print('최근 많은사람들이 열광한 것 중 하나야')
    elif num==4 :
        print('손목이 아파')
    elif num==5 :
        print('영어')
    elif num==6 :
        print('식빵')
    elif num==7 :
        print('스포츠')
    elif num==8 :
        print('y앞뒤로 볼과 볼이 있다')
    elif num==9 :
        print('6명 또는 9명이 같이 즐겨')
    elif num==10 :
        print('ymca 윌리엄 모건이 만들었어')
    elif num==11 :
        print('체육관 혹은 바닷가에서 즐길 수 있어')
    elif num==12 :
        print('최근 도쿄 올림픽에서 9년만에 4강에 올랐어')
    elif num==13 :
        print('네트 스포츠의 한 종류야')
    elif num==14 :
        print('총 10글자로 구성되어 있다')
    else :
        print('두개의 단어로 구성되어있고, 각각 뜻이 있다')

    a = a+1

print()
print('이제 암호의 답을 적을 시간입니다. 기회는 세번뿐이니 신중하게 선택하세요.')

ans = 'volleyball'
count = 1

while count <= 3 :
    inputPw = input('암호를 입력하세요 :  ')

    if inputPw != ans :
        if count == 3 :
            print('로그인 횟수를 초과하였습니다. 실패입니다..')
            break
        print('암호를 다시 확인하세요')
        count = count + 1

    else :
          print('정답입니다')
          print()
          print('주소 : taedhwlddjrpdla.neocities.org')
          break
    print()
