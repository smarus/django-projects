#!/usr/bin/python
# -*- coding: ascii -*-

import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore

nytimes_com = '''This New Liquid Is Magnetic, and Mesmerizing

Scientists have created ?soft? magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker?s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here

args = sys.argv
dir = args[1]

map = {'bloomberg.com': bloomberg_com,
       'nytimes.com': nytimes_com}

lis = []


def valid_url(string):
    if string.find('.') != -1:
        return True
    return False


def save_file(content, file_name):
    with open(dir + '/' + file_name, 'w', encoding='utf-8') as f1:
        f1.write(content)


def check_file(file_name):
    boolen = os.path.isfile(dir + '/' + file_name)
    # print(boolen)
    return boolen


def print_data():
    if len(lis) > 0:
        lis.pop()
        print(lis.pop())


def check_https(url):
    if url.find('https://') != -1:
        return url
    else:
        return 'https://' + url


def parse_html(html):
    soup = BeautifulSoup(html.content, 'html.parser')
    text = soup.get_text(separator='\n', strip=True)
    # text_tags = soup.find_all('p')
    # text.append([i.text for i in text_tags])
    # text_tags = soup.find_all('a')
    # text.append([i.text for i in text_tags])
    # text_tags = soup.find_all('ul')
    # text.append([i.text for i in text_tags])
    # text_tags = soup.find_all('ol')
    #  text.append([i.text for i in text_tags])
    # text_tags = soup.find_all('li')
    # text.append([i.text for i in text_tags])
    return Fore.BLUE +text


def print_cached_data(file_name):
    with open(dir + '/' + file_name, 'r', encoding='utf-8') as f1:
        data = f1.read()
        lis.append(data)
        print(data)


def main():
    while True:
        word = input("Write cite: ")
        if word == "exit":
            break
        if word == 'back':
            print_data()

        if valid_url(word):
            file_name = word.split('.')[0]
            url = check_https(word)
            if check_file(file_name):
                print_cached_data(file_name)
            else:
                r = requests.get(url)
                text = parse_html(r)
                save_file(text, file_name)
                print(text)
                lis.append(text)
        elif check_file(word):
            print_cached_data(word)
        else:
            print("Error: Incorrect URL")


if not os.path.exists(dir):
    os.mkdir(dir)

main()
