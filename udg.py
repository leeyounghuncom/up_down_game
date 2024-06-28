import random

# 이전 게임 플레이어 최고 시도 횟수 초기화
pc = 0

while True :

    print(f"이전 게임 플레이어 최고 시도 횟수: {pc}")

    # 컴퓨터는 1부터 100 사이의 랜덤한 숫자를 생성합니다.
    bot = random.randint(1, 100)

    # 플레이어가 컴퓨터의 숫자를 정확히 맞히면 시도한 횟수를 알려줍니다.
    nc = 0 #초기화

    # 플레이어가 숫자를 맞힐 때까지 위 과정을 반복합니다.
    while True:

        try:
            #시도 횟수 1씩 증가
            nc += 1

            # 플레이어는 숫자를 입력하고,
            guest = int(input("숫자를 입력하세요: "))

            # 플레이어가 입력한 숫자가 범위를 벗어날 경우, 적절한 안내 메시지를 출력하여 유효한 범위 내의 숫자를 입력하도록 유도하세요.
            if not 1 <= guest <= 100:
                print("유효한 범위 내의 숫자를 입력하세요 1~100")
                continue

            # 입력한 숫자와 컴퓨터의 숫자를 비교하여 "업" 또는 "다운" 힌트를 제공합니다.
            if (bot > guest):
                print("업")
            elif (bot < guest):
                print("다운")
            else:
                print("맞았습니다")
                break

            print(f"시도한 횟수: {nc}")
            # 게임이 종료될 때 플레이어의 최고 시도 횟수를 기록하고, 다음 게임에서 이를 표시하는 기능을 구현하세요.
            if nc > pc :
                pc = nc

            # 모니터링
            print(f"봇: {int(bot)} 게스트: {int(guest)} 시도갯수: {int(nc)}")

        except ValueError:
            print("숫자만 입력하시오")

    # 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가하세요.
    rsg = input("다시 하시겠습니까? (y/n):")
    if rsg != 'y':
        print('게임을 종료합니다')
        break