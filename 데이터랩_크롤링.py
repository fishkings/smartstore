# 네이버 쇼핑몰 크롤링_version(1.0.2)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

from openpyxl import Workbook
from openpyxl.styles import Alignment
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE  # openpyxl에서 허용되지 않는 단어들 

import time
import csv
import random
import pyautogui

num = int(pyautogui.prompt("첫 번째 카테고리 번호를 입력하세요."))

wb = Workbook()
sheet = wb.active

def most_searching(total_lst,found_error):
    for i in range(25) :  # 버튼이 25개
        if driver.find_elements(By.CSS_SELECTOR, ".rank_top1000 .link_text"):
            ranks = driver.find_elements(By.CSS_SELECTOR, ".rank_top1000 .link_text")
            time.sleep(.6)  # 이거 조절 안하면 오버래핑  -> 21\n  이런식으로 나옴
            for rank in ranks:
                try :
                    text = rank.text
                    span = rank.find_element(By.CSS_SELECTOR,".rank_top1000_num")
                    text = text.replace(span.text, "").strip()
                    if ILLEGAL_CHARACTERS_RE.search(text):
                     print("ILLEGAL_CHARACTERS")  # 허용되지 않는 단어들 추출
                     continue
                    total_lst.append(text)
                except:
                     print("페이지 25개 이하")
                     found_error = True
                     break
            if found_error :
                break
        else : break
        driver.find_element(By.CSS_SELECTOR, ".btn_page_next").click()
    return set(total_lst)

# 인기 검색어 대표 타이틀
def insite_title() :
    time.sleep(.4)
    return driver.find_element(By.CSS_SELECTOR, ".section .insite_title strong").text



# 브라우져 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())  # Chrome driver 자동 업데이트
driver = webdriver.Chrome(service=service, options=chrome_options)
# driver.maximize_window() #화면 최대화

# 해당 웹페이지로 이동
driver.get("https://datalab.naver.com/shoppingInsight/sCategory.naver")
driver.implicitly_wait(10)

dropdowns = driver.find_elements(By.CSS_SELECTOR,".set_period.category  .select")
first_option = dropdowns[0].find_elements(By.CSS_SELECTOR,"li .option")[num]

time_randome = random.random() # 랜덤 값을 주어서 봇 방지
found_error = False # 2중 for문 break

# input checkbox 선택
lbls = driver.find_elements(By.CSS_SELECTOR,".lbl.active")
for i in range(3):
    lbls[i].click()

# 1번째 카테고리 선택
driver.execute_script('arguments[0].click();',dropdowns[0])
time.sleep(time_randome)
driver.execute_script('arguments[0].click();',first_option)
time.sleep(time_randome)

# 2번째 카테고리 선택
second_options = dropdowns[1].find_elements(By.CSS_SELECTOR,"li .option")
for idx_s,second_option  in enumerate(second_options):
    driver.execute_script('arguments[0].click();',dropdowns[1])
    time.sleep(time_randome)
    driver.execute_script('arguments[0].click();',second_option)
    time.sleep(time_randome)

    # 3번째 카테고리 선택
    dropdowns = driver.find_elements(By.CSS_SELECTOR,".set_period.category  .select") # 3분류가 새로 생겨서 업데이트
    if(len(dropdowns)==6):
        third_options = dropdowns[2].find_elements(By.CSS_SELECTOR,"li .option")
        for idx_t,third_option  in enumerate(third_options):
            driver.execute_script('arguments[0].click();',dropdowns[2])
            time.sleep(time_randome)
            driver.execute_script('arguments[0].click();',third_option)
            time.sleep(time_randome)
            driver.find_elements(By.CSS_SELECTOR,".btn_submit")[0].click()
            time.sleep(time_randome)
            print(f"{num} - {idx_s} - {idx_t} {insite_title()} 항목")

            total_lst = []
            total_lst.append(insite_title())

            most_searching(total_lst,found_error) # 대표 타이틀 / 인기 검색어 불러오기
            print(len(total_lst))
            sheet.append(list(total_lst))

    else :
            print(f"{num} - {idx_s} {insite_title()} 항목")
            total_lst = []
            print(insite_title())
            driver.find_elements(By.CSS_SELECTOR,".btn_submit")[0].click()
            total_lst.append(insite_title())
            most_searching(total_lst,found_error) # 대표 타이틀 / 인기 검색어 불러오기
            sheet.append(total_lst)

wb.save(f"네이버쇼핑몰크롤링\Category{num}_search.csv")
