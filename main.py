import time
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
driver = webdriver.Chrome('D:\바탕화면\chromedriver\chromedriver.exe')
driver.get('https://www.imdb.com/title/tt4633694/reviews?ref_=tt_urv')  #이부분만 바꾸면 됨
driver.implicitly_wait(5)
reviews = []

def get_review():
    datas = soup.select('#main > section > div.lister > div.lister-list >div')
    for data in datas:
        review = data.select_one(
            'div.review-container > div.lister-item-content > div.content > div.text.show-more__control').text
        reviews.append(review)
    dataframe=pd.DataFrame(reviews)
    dataframe.to_csv("Spider-ManIntotheSpider-Verse.csv")

while True:
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="load-more-trigger"]').click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
    except:
        break


get_review()

driver.close()
