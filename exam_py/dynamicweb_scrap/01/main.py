from bs4 import BeautifulSoup
import requests
import time
# import urllib.request

nvsearch_url = 'https://datalab.naver.com/keyword/realtimeList.naver'
r = requests.get(nvsearch_url)

soup = BeautifulSoup(r.text, 'lxml')
print(soup)

'''
payload = {'datetime' : '2018-07-30T09:00:00'}
html = requests.get(url, 'lxml')
with open('naversearch.html', 'w') as nv:
    nv.write(html.text)
'''


