from selenium import webdriver
from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time

#창 안띄우고 크롤링
options=webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

browser=webdriver.Chrome(options=options)
browser.maximize_window()
url='https://www.google.com/search?q=apple&tbm=isch&chips=q:%EC%95%A0%ED%94%8C,g_1:%EB%A1%9C%EA%B3%A0:bOlIq3H5zMc%3D&hl=ko&sa=X&ved=2ahUKEwiH742Kq_WCAxW9ulYBHWABCBoQ4lYoAHoECAEQKw&biw=1329&bih=953'
browser.get(url)

def fn_soup(res):
    soup=BeautifulSoup(res, 'lxml')

    images=soup.find_all('div', attrs={'class' : 'isv-r PNCib ViTmJb BUooTd'})
    # print(len(images))

    for idx, image in enumerate(images):
        title=image.find('div', attrs={'class' : 'zbRPDe M2qv4b P4HtKe'}).get_text()
        print(idx + 1, title)

#이전 스크롤 높이
prev_height=browser.execute_script('return document.body.scrollHeight')
# print(prev_height)
while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    curr_height=browser.execute_script('return document.body.scrollHeight')
    if prev_height == curr_height:
        break
    prev_height = curr_height

res=browser.page_source
fn_soup(res)
time.sleep(1)


