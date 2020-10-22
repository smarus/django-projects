import requests

from bs4 import BeautifulSoup

subtitle = int(input())
link = input()

r = requests.get(link)
soup = BeautifulSoup(r.content, 'html.parser')
list = soup.find_all('a')
print(list[subtitle - 1].get('href'))

