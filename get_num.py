import requests
from bs4 import BeautifulSoup


def get_current_draw_num():
    # 웹 페이지의 URL
    url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'

    # HTTP GET 요청 보내고 응답 받기
    response = requests.get(url)

    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # h4 > strong 요소 선택
    h4_strong_element = soup.select_one('h4 > strong')

    # h4 > strong 요소의 텍스트 가져오기
    text = h4_strong_element.text

    # 마지막 글자 제외한 문자열 추출
    text = text[:-1]

    # 문자열을 숫자 리스트로 변환
    number = int(text)

    # 결과 반환
    return number


def get_last_two_weeks_numbers(cur_num):
    # 웹 페이지의 URL
    url_1 = 'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo='+str(cur_num)
    url_2 = 'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo='+str(cur_num-1)

    # HTTP GET 요청 보내고 응답 받기
    response_1 = requests.get(url_1)
    response_2 = requests.get(url_2)

    # BeautifulSoup을 사용하여 HTML 파싱
    soup_1 = BeautifulSoup(response_1.text, 'html.parser')
    soup_2 = BeautifulSoup(response_2.text, 'html.parser')

    # 결과 값을 저장할 리스트 초기화
    result_values_1 = []
    result_values_2 = []

    # .win > p > span 요소 선택
    win_elements_1 = soup_1.select('.win p span')
    win_elements_2 = soup_2.select('.win p span')

    # 결과 값을 리스트에 저장
    for win_element in win_elements_1:
        result_values_1.append(int(win_element.text))
    for win_element in win_elements_2:
        result_values_2.append(int(win_element.text))
    # 결과 반환
    return result_values_1, result_values_2
