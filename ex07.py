import requests
from bs4 import BeautifulSoup

url='https://www.google.com/search?q=apple&tbm=isch&chips=q:%EC%95%A0%ED%94%8C,g_1:%EB%A1%9C%EA%B3%A0:bOlIq3H5zMc%3D&hl=ko&sa=X&ved=2ahUKEwiH742Kq_WCAxW9ulYBHWABCBoQ4lYoAHoECAEQKw&biw=1329&bih=953'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
res=requests.get(url, headers=header)
res.raise_for_status()

soup=BeautifulSoup(res.text, 'lxml')

images=soup.find_all('div', attrs={'class' : 'isv-r PNCib ViTmJb BUooTd'})
# print(len(images))

for idx, image in enumerate(images):
    title=image.find('div', attrs={'class' : 'zbRPDe M2qv4b P4HtKe'}).get_text()
    print(idx + 1, title)