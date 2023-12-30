# 연속된 3개의 숫자가 있는지 확인하는 함수
def has_consecutive_numbers_more_than_three(lst):
    if len(lst) < 3:
        return False
    lst.sort()
    for i in range(len(lst) - 2):
        if lst[i] == lst[i+1] - 1 == lst[i+2] - 2:
            return True
    return False


# 10의 자리 수가 같은 요소가 3개 이상인지 확인하는 함수
def has_same_three_tens(lst):
    if len(lst) < 3:
        return False
    tens_dict = {}  # 10의 자리 수를 키로, 출현 횟수를 값으로 하는 딕셔너리

    for number in lst:
        tens_place = number // 10  # 10의 자리 수 계산

        if tens_place in tens_dict:
            tens_dict[tens_place] += 1
        else:
            tens_dict[tens_place] = 1

    # 딕셔너리에서 값이 3 이상인 키가 있는지 확인
    for count in tens_dict.values():
        if count >= 3:
            return True

    return False


# 이전 회차와 같은 숫자가 3개 이상 있는지 확인하는 함수
def has_same_with_last_week(num, last_week, two_weeks_ago, last, two_ago):
    if num in last_week:
        last +=1
    if num in two_weeks_ago:
        two_ago +=1
    return last, two_ago
