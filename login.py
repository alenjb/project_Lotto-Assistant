from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

import account

# webdriver.Chrome 대신 Chrome으로 수정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def login_and_buy(expected_nums_tuple):
    try:
        # 웹페이지 열기
        driver.get("https://dhlottery.co.kr/user.do?method=login&returnUrl=")

        # 입력 필드에 값 입력
        user_id = account.user_id
        password = account.password

        driver.find_element(By.ID, "userId").send_keys(user_id)
        driver.find_element(By.NAME, "password").send_keys(password)

        # 로그인 버튼 클릭
        driver.find_element(By.CSS_SELECTOR, 'a.btn_common.lrg.blu').click()
        driver.get("https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LO40")

        # 대기 시간을 10초로 설정하고 iframe이 나타날 때까지 기다립니다.
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "ifrm_tab")))

        for expected_nums in expected_nums_tuple:
            # 예상 번호들을 선택(페이지에서 클릭)
            for num in expected_nums:
                element_id = f"check645num{num}"
                driver.execute_script(f"document.getElementById('{element_id}').click();")
                time.sleep(0.1)  # 페이지 업데이트를 기다리기 위해 추가

            # 확인 버튼을 클릭
            driver.find_element(By.ID, 'btnSelectNum').click()


        # 구매하기 버튼을 클릭
        driver.find_element(By.ID, 'btnBuy').click()

        # 확인 버튼 클릭
        # JavaScript로 확인 버튼 클릭
        js_confirm_code = """document.querySelector("#popupLayerConfirm > div > div.btns > input:nth-child(1)").click();"""
        js_exit_code = """document.querySelector("#closeLayer").click();"""
        driver.execute_script(js_confirm_code)
        driver.execute_script(js_exit_code)

    finally:
        # 크롬 창 닫기
        driver.quit()