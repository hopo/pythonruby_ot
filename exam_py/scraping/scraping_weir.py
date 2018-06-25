import requests
from bs4 import BeautifulSoup

url = "https://news.google.co.kr/"

response = requests.get(url)

print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')

#ls = soup.select('li.list-group-item')
# print(ls)
