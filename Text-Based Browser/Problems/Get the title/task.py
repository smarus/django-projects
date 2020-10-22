import requests

from bs4 import BeautifulSoup


r = requests.get(input())
soup = BeautifulSoup(r.content, 'html.parser')
paragraphs = soup.find_all('h1')
par = [i.text for i in paragraphs]
print(par[0])