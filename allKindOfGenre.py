import csv

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.imdb.com/feature/genre/?ref_=nv_ch_gr', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

f=open('allGenre.csv', 'w',encoding='utf-8',newline="")
wr=csv.writer(f)
genres=soup.select('#sidebar > div:nth-child(12) > span > div > div > div > div > div > div >div ')
for genre in genres:
    g=genre.select_one('div > a')
    print(g.text)
    wr.writerow([g.text])

f.close()


