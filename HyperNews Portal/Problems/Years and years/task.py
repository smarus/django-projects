import json


years = {2020: "leap year", 2021: "regular year", 2022: "regular year",
         2023: "regular year", 2024: "leap year"}
 # json = {"created": "2020-02-09 14:15:10", "text": "Text of the news 1", "title": "News 1", "link": 1}, {"created": "2020-02-10 14:15:10", "text": "Text of the news 2", "title": "News 2", "link": 2}, {"created": "2020-02-09 16:15:10", "text": "Text of the news 3", "title": "News 3", "link": 3}
# convert years to JSON string

years_json = json.dumps(years,indent=4)
with open('/Users/macbookpro/PycharmProjects/HyperNews Portal/HyperNews Portal/task/news.json', 'r') as file:
    js = json.load(file)
    dek= {'name': 'fdsfsdf','title': 'ddd','link': '32','created': 'd3232'}
    js.append(dek)
    print(js)
