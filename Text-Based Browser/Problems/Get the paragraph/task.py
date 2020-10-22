import requests

from bs4 import BeautifulSoup

word = input()
r = requests.get(input())
soup = BeautifulSoup(r.content, 'html.parser')
paragraphs = soup.find_all('p')
par = [i.text for i in paragraphs]
for i in par:
    if word in i:
        print(i)
        break
