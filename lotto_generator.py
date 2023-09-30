import random
import requests
from bs4 import BeautifulSoup

import control_num
import get_num

# 현재 회차 번호 가져오기
cur_num = get_num.get_current_draw_num()
last_week, two_weeks_ago = get_num.get_last_two_weeks_numbers(cur_num)


# 로또 번호 생성 함수
def lotto_generator():
    lotto_numbers = []
    last =0
    two_ago = 0
    while len(lotto_numbers) < 6:
        # 로또 번호 추출
        number = random.randint(1, 45)
        last, two_ago = control_num.has_same(number, last_week, two_weeks_ago, last, two_ago)
        # 조건 1: 지난 주와 지지난 주의 당첨번호와 3개 이상 겹치지 않게
        if last <3 and two_ago <3:
            # 조건 2: 3개 연달아서 안 나오게
            if (
                    len(lotto_numbers) < 3 or
                    control_num.has_consecutive_numbers(lotto_numbers) is False
            ):
                # 조건 3: 같은 번호대에서 3개까지만 나오게
                if len(lotto_numbers) < 3 or control_num.has_same_three_tens(lotto_numbers) is False:
                    # 추출 번호를 리스트에 추가
                    lotto_numbers.append(number)
                else:
                    print("다시하는 중1")
                    continue
            else:
                print("다시하는 중2")
                continue
        else:
            if last == 3:
                last -=1
            if two_ago == 3:
                two_ago -=1
            print("다시하는 중3", last, two_ago, "num: ",number)
            continue

    return lotto_numbers


# 로또 번호 생성 및 출력
print("-------------------- 제", cur_num, "회 로또 예상 번호 --------------------")
for j in range(1, 3):
    print(j, "번째 로또 번호:", sorted(lotto_generator()))




