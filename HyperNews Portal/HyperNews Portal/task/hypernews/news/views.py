import operator
from itertools import groupby

from django.shortcuts import render
import json
from datetime import datetime
from random import randint
from django.views import View
from operator import itemgetter
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import redirect


# Create your views here.
class MainPageView(View):
    def get(self, request, *args, **kwargs):
        posts = get_json()

        all_news = []
        q = ""
        if "q" in request.GET:
            q = request.GET['q']

        for post in posts:
            if q in post["title"]:
                post["fecha"] = post["created"][:10]
                all_news.append(post)

        dates = set()
        for post in all_news:
            date = post["created"][:10]
            dates.add(date)

        context = {
            "all_news": all_news,
            "order": sorted(dates, reverse=True),
        }
        return render(request, "news/main_page.html", context=context)


class MainPageAllView(View):
    def get(self, request, *args, **kwargs):
        return redirect('/news/')


class NewsPageView(View):
    def get(self, request, news_link, *args, **kwargs):
        news = get_json()
        print(news_link)
        print(news)
        for key in news:
            if int(key['link']) == int(news_link):
                context = {'news_item': key}
                return render(request, 'news/index.html', context=context)
        raise Http404


class CreatePageView(View):
    def post(self, request, *args, **kwargs):
        title = request.POST('title')
        text = request.POST('text')
        news = get_json()
        link = randint(1, 1000000)
        created = datetime.strptime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        new_news = {
            'title': title,
            'text': text,
            'link': link,
            'created': created
        }
        news.append(new_news)
        save_json(json)
        return redirect('/news/')


class NewsCreatePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'news/create_form.html')

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        text = request.POST.get('text')
        news = get_json()
        link = randint(1, 1000000)
        created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_news = {
            'title': title,
            'text': text,
            'link': link,
            'created': created
        }
        news.append(new_news)
        print(news)
        save_json(news)
        return redirect('/news/')


def get_json():
    with open(settings.NEWS_JSON_PATH, 'r') as file:
        return json.load(file)


def save_json(json_dict):
    with open(settings.NEWS_JSON_PATH, 'w')as file:
        json_str = json.dumps(json_dict, indent=4)
        file.write(json_str)
        pass
