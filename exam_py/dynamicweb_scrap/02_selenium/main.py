from selenium import webdriver
from bs4 import BeautifulSoup

# nvsearch_url = 'https://datalab.naver.com/keyword/realtimeList.naver'
nvsearch_url = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=2018-07-30T09:00:00'

driver = webdriver.Firefox(executable_path='../geckodriver')
driver.get(nvsearch_url)
res = driver.execute_script('return document.documentElement.outerHTML')
driver.quit()

soup = BeautifulSoup(res, 'lxml')


# payload = {'datetime' : '2018-07-30T09:00:00'}
with open('../naversearch.html', 'w') as nv:
    nv.write(soup.text)

