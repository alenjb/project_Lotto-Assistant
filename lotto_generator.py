import random
import sys

import requests
from bs4 import BeautifulSoup

import control_num
import get_num
import login

# 현재 회차 번호 가져오기
cur_num = get_num.get_current_draw_num()
last_week, two_weeks_ago = get_num.get_last_two_weeks_numbers(cur_num)


# 로또 번호 생성 함수
def lotto_generator(sets_number):
    result_lists = []
    # 구매 세트 수만큼 반복
    for _ in range(sets_number):
        lotto_numbers = []
        # 지난 회차 번호와 겹치는 개수
        last_duplicated = 0
        # 지지난 회차 번호와 겹치는 개수
        two_ago_duplicated = 0

        # 생성가능한 숫자들
        capable_numbers = list(range(1, 46))
        while len(lotto_numbers) < 6:
            # 생성가능한 숫자들에서 로또 번호 추출
            number = random.choice(capable_numbers)
            last_duplicated, two_ago_duplicated = control_num.has_same_with_last_week(number, last_week, two_weeks_ago, last_duplicated, two_ago_duplicated)
            # 조건 1: 지난 주와 지지난 주 회차와 같은 숫자가 3개 이상 존재하지 않는다.
            if last_duplicated < 3 and two_ago_duplicated < 3:
                # 조건 2: 3개 이상의 숫자가 연속되어 나오지 않는다.
                if control_num.has_consecutive_numbers_more_than_three(lotto_numbers) is False:
                    # 조건 3: 추첨 숫자 중 같은 10의 자리 숫자가 3개 이상 존재하지 않는다.
                    if control_num.has_same_three_tens(lotto_numbers) is False:
                        # 추출 번호를 리스트에 추가
                        lotto_numbers.append(number)
                        capable_numbers.remove(number)
                    # 지난 주와 지지난 주의 당첨번호와 3개 이상 겹치지 않고 3개 이상의 숫자가 연속되지 않지만 같은 10번대의 숫자가 3개인 경우
                    else:
                        continue
                # 지난 주와 지지난 주의 당첨번호와 3개 이상 겹치지 않지만 3개 이상의 숫자가 연속된 경우
                else:
                    continue
            # 지난 주와 지지난 주의 당첨번호와 3개 이상 겹치는 경우
            else:
                # 지난 주 번호와 겹친 경우
                if last_duplicated == 3:
                    last_duplicated -= 1
                    capable_numbers.remove(number)
                # 지지난 주 번호와 겹친 경우
                if two_ago_duplicated == 3:
                    two_ago_duplicated -= 1
                    capable_numbers.remove(number)
                continue
        result_lists.append(lotto_numbers)
    return result_lists


# 로또 번호 생성 및 출력
# 구매할 세트 수를 입력받기
received_sets_number= int(input("구매할 세트 수를 입력하세요: "))
buy_amount = 1000 * received_sets_number
expected_nums = sorted(lotto_generator(received_sets_number))
print("번호 추출이 완료되었습니다.")
login.login_and_buy(expected_nums)
# 결과를 출력
print("-------------------- 제", cur_num, "회 로또 예상 번호 --------------------")
for i, j in zip(range(1, len(expected_nums)+1), expected_nums):
    print(i, "번째 로또 번호:", j)
print("총 ", format(buy_amount, ','), "원어치 로또를 구매를 완료하였습니다.")


