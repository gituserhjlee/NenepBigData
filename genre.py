import csv

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.imdb.com/title/tt10059518/?ref_=nv_sr_srsg_0', headers=headers) #영화마다 주소 변경해주기
soup = BeautifulSoup(data.text, 'html.parser')

f=open('genre.csv', 'a',encoding='utf-8',newline="")
wr=csv.writer(f)
title=soup.select_one('#title-overview-widget > div.vital > div.title_block > div > div.titleBar > div.title_wrapper > h1').text
genre1 = soup.select_one(' #title-overview-widget > div.vital > div.title_block > div > div.titleBar > div.title_wrapper > div> a:nth-child(4) ').text   #영화마다 장르 개수에 따라서 선택하기
genre2 = soup.select_one(' #title-overview-widget > div.vital > div.title_block > div > div.titleBar > div.title_wrapper > div> a:nth-child(5) ').text
# genre3 = soup.select_one(' #title-overview-widget > div.vital > div.title_block > div > div.titleBar > div.title_wrapper > div> a:nth-child(6) ').text
print(title,genre1)
# wr.writerow([title, genre1])
wr.writerow([title, genre1, genre2])
# wr.writerow([title, genre1, genre2, genre3])
f.close()


