import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import os
import glob


def crawling():
    # 크롬 옵션 설정
    chrome_options = webdriver.ChromeOptions()

    # WebDriver 설정
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # URL로 이동
    url = "https://taas.koroad.or.kr/gis/mcm/mcl/initMap.do?menuId=GIS_GMP_STS_NTS#"
    driver.get(url)

    # 페이지 요소와 상호작용
    select1 = driver.find_element(By.CSS_SELECTOR, 'a.left-icon02')
    select1.click()

    time.sleep(1)

    # 시작 연도 선택 (2021)
    select2 = Select(driver.find_element(By.ID, 'ptsRafYearStart'))
    select2.select_by_value("2021")

    # 종료 연도 선택 (2023)
    select3 = Select(driver.find_element(By.ID, 'ptsRafYearEnd'))
    select3.select_by_value("2023")

    # 지역 선택 (서울특별시)
    select4 = Select(driver.find_element(By.ID, 'ptsRafSido'))
    select4.select_by_value("11")

    # 세부 지역 선택 (서울 강서구)
    select5 = Select(driver.find_element(By.ID, 'ptsRafSigungu'))
    select5.select_by_value("11545")

    # 사고유형 체크박스 선택
    checkbox1 = driver.find_element(By.CSS_SELECTOR, 'input[name="ACDNT_GAE_CODE"][value="02"]')
    checkbox1.click()

    checkbox2 = driver.find_element(By.CSS_SELECTOR, 'input[name="ACDNT_GAE_CODE"][value="03"]')
    checkbox2.click()

    checkbox3 = driver.find_element(By.CSS_SELECTOR, 'input[name="ACDNT_GAE_CODE"][value="04"]')
    checkbox3.click()

    # 검색 버튼 클릭
    search_button = driver.find_element(By.CSS_SELECTOR, 'a.btn-search')
    search_button.click()

    time.sleep(5)  # 검색 결과 로딩 시간 대기

    # 데이터가 로드되기 전에 스크롤을 끝까지 내려서 모든 데이터를 로딩
    select7 = driver.find_element(By.CSS_SELECTOR, 'a.btn-minibox')
    select7.click()

    time.sleep(5)  # 페이지 로드 대기

    # 새 창이나 탭이 열렸는지 확인하고 전환
    main_window = driver.current_window_handle
    all_windows = driver.window_handles

    for window in all_windows:
        if window != main_window:
            driver.switch_to.window(window)  # 새 창으로 전환

    # 엑셀 다운로드 버튼 클릭
    select8 = driver.find_element(By.CSS_SELECTOR, 'input.pop-btn04')
    select8.click()

    # 다운로드가 완료될 때까지 대기 (필요에 따라 시간을 조정)
    time.sleep(20)

    # 다운로드된 엑셀 파일을 찾기 (가장 최근에 다운로드된 파일)
    list_of_files = glob.glob(os.path.join(os.path.expanduser("~"), "Downloads", "*.xls"))  # 기본 다운로드 폴더 사용
    if not list_of_files:
        print("엑셀 파일을 찾을 수 없습니다.")
    else:
        # 가장 최근에 생성된 파일 찾기
        latest_file = max(list_of_files, key=os.path.getctime)
        print(f"가장 최근에 다운로드된 파일: {latest_file}")

        df = pd.read_html(latest_file)[0]
        df.to_excel("accidentInfoList.xlsx")
        print(f"엑셀 파일이 accidentInfoList.xlsx로 변환되었습니다.")

    # WebDriver 종료
    driver.quit()
    return

