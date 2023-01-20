import urllib.request
from datetime import datetime, timedelta
import re
import requests
import lxml
import time
from bs4 import BeautifulSoup
import wget
import os
import json
from urllib.request import Request, urlopen
import sqlite3
from tomita.tomita import tomita



def function_date (date):
    date = date.replace('T', ' ')
    date = date.split(".")[0]
    return date
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
def parser():
    con = sqlite3.connect("sema.db")
    global count
    count = 0

    url_news = 'https://novostivolgograda.ru/news'
    url = 'https://novostivolgograda.ru/'
    news_text = ''        # хранит содержание новости
    way_to_page = []      # хранит ссылки на все страницы с новостями
    count = 0             # счетчик новости
    date = ""             # дата
    link_news = ""        # ссылка новости
    title= ""             # хранит заголовок новости
    main_text = ""        # хранит полный текст новости
    id_news = 0           # хранит уникальный ID новости
    flag = False

    for j in range(5):
        for i in range(1, 99):
            if flag == True:
                break 
            way_to_page.append("https://novostivolgograda.ru/api/site/matters?date_start=&date_end=&page=" + str(i))

            opener = urllib.request.URLopener()
            opener.addheader('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36')

            filename, headers = opener.retrieve(way_to_page[i-1], "save.json")

            with open('save.json', 'r', encoding='utf-8') as file_page:    # читает файл
                text_page_json = json.load(file_page)

            for txt_info in text_page_json['matters']:
                try:
                    count += 1
                    print("Новость " + str(count))
                    id_news = txt_info['id']
                    print (" ID новости: " + str(txt_info['id']))
                    date = txt_info["published_at"]
                    date = function_date(date)
                    print(" Дата: " + str(date))
                    link_news = "https://novostivolgograda.ru" + txt_info['path']  # переменная для хранения полной ссылки новости
                    print(" Сылка на новость: " + str(link_news))
                    title = txt_info["lead"]
                    print(txt_info["lead"])

                    response = requests.get(link_news)
                    soup = BeautifulSoup(response.text, 'lxml')
                    main = soup.find(class_='relative desktop-cols-3')
                    texts_default = main.find_all('p')

                    news_text = ""

                    for text in texts_default:
                        news_text += text.text + "\n"

                    main_text = str(news_text)
                    print(" Содержание: \n" + str(news_text))
                    try:
                        with sqlite3.connect("sema.db") as con:
                            cur = con.cursor()
                            cur.execute("INSERT into post(id_post, title, date, link, text) values (?, ?, ?, ?, ?)", (int(id_news), str(title), str(date), str(link_news), str(news_text)))
                            con.commit()
                            msg = 'success'
                            tomita(news_text, id_news, date)
                    except:
                        flag = True
                        msg = 'not success'
                        break
                except:
                    pass
                
            # В КОНЦЕ УДАЛЯЕМ ФАЙЛИК save.json (ЖЕЛАТЕЛЬНО В КАЖДОМ ЦИКЛЕ!)
            os.remove("save.json")
    
    return msg
                
            


