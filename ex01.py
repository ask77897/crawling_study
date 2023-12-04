import requests
import json
import streamlit as st
from bs4 import BeautifulSoup

url='http://www.cgv.co.kr/movies/?lt=1&ft=0'
res=requests.get(url)
res.raise_for_status()
# print(res.text)

soup=BeautifulSoup(res.text, 'lxml')
title1=soup.title
title=soup.title.get_text()
body=soup.body
body=soup.body.get_text()

# print(title, title1)
# print(body)

# print(soup.a)
# print(soup.a.attrs)
# print(soup.a['href'])

chart=soup.find('div', attrs={'class' : 'sect-movie-chart'})
# print(chart)
movies=chart.find_all('li')
# print(len(movies))
json_movies=[]

# print("_"*50)
for movie in movies:
    rank=movie.find('strong', attrs={'class' : 'rank'}).get_text()
    title=movie.find('strong', attrs={'class' : 'title'}).get_text()
    image=movie.find('img')['src']
    percent=movie.find('strong', attrs={'class':'percent'})
    percent=percent.span.get_text()
    link='https://www.cgv.co.kr' + movie.find('a', attrs={'class' : 'link-reservation'})['href']
    # print(f'예매순위 : {rank}')
    # print(f'영화제목 : {title}')
    # print(f'영화포스터 : {image}')
    # print(f'예매율 : {percent}')
    # print(f'예매하기 : {link}')
    # print('_' * 50)
    
    json_movie={'rank':rank, 'title':title, 'image':image, 'percent':percent, 'link':link}
    json_movies.append(json_movie)
    
    
# with open('movie.json', 'w', encoding='utf-8') as file:
#     json.dump(json_movies, file, indent='\t', ensure_ascii=False)
    
# print(len(json_movies))

st.set_page_config(layout='wide')
st.header('CGV MovieChart')
idx=0
for row in range(0, 5):
    cols=st.columns(4)
    for col in cols:
        if idx > 18:
            break
        else:
            movie=json_movies[idx]
            col.image(movie['image'])
            col.write(movie['title'])
            idx += 1
        