from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url='https://flight.naver.com/'
browser=webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(1)

#가는날 버튼 선택
begin_date=browser.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[4]/div/div/div[2]/div[2]/button[1]')
begin_date.click()
time.sleep(1)

#가는 날짜 선택
day25=browser.find_elements(By.XPATH, '//b[text()="25"]')
day25[0].click()
time.sleep(1)
#오는 날짜 선택
day26=browser.find_elements(By.XPATH, '//b[text()="26"]')
day26[0].click()
time.sleep(1)

#도착지 선택
arrival=browser.find_element(By.XPATH, '//b[text()="도착"]')
arrival.click()
time.sleep(1)

domestic=browser.find_element(By.XPATH, '//button[text()="국내"]')
domestic.click()
time.sleep(1)

jeju=browser.find_element(By.XPATH, '//i[text()="제주국제공항"]')
jeju.click()
time.sleep(1)

#항공권검색
search=browser.find_element(By.XPATH, '//span[text()="항공권 검색"]')
search.click()
time.sleep(10)

first='//div[@class="domestic_Flight__sK0eA result"]'
elem=WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, first)))
print(elem.text)