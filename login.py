from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

import account

# webdriver.Chrome 대신 Chrome으로 수정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

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
    WebDriverWait(driver, 2).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "ifrm_tab")))

    # iframe 내부에서 라벨 찾기 (for 속성 값이 "check645num23"인 경우)
    label_element = driver.find_element(By.CSS_SELECTOR, 'label[for="check645num23"]')

    # 라벨의 텍스트 변경하기
    new_text = "23"
    driver.execute_script(f"arguments[0].innerText = '{new_text}';", label_element)
    time.sleep(2)
    # 라벨의 텍스트가 변경되었는지 검증하기
    updated_label_element = driver.find_element(By.CSS_SELECTOR, 'label[for="check645num23"]')
    print(updated_label_element.text)

finally:
    print("end")
    # 크롬 창 닫기
    # driver.quit()
