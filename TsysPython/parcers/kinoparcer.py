import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter
import time
import codecs

# for num in range(1, 10):
#         url = 'https://www.kinopoisk.ru/lists/navigator/?page=' + str(num) + '&sort=popularity&quick_filters=available_online&tab=online'# url страницы
#         r = requests.get(url)
#         soup = BeautifulSoup(r.text, 'lxml')
#         for n in range(50):
#             quotes = soup.findAll("p", class_='selection-film-item-meta__name')[n].text
#             print(quotes)
#         print(num)
#         print(url)
#
# # n = 0
# url = 'https://www.kinopoisk.ru/lists/navigator/?sort=popularity&quick_filters=available_online&tab=online'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# for n in range(50):
#     quotes = soup.findAll("p", class_='selection-film-item-meta__name')[n].text
# #     print(quotes)
#
# workbook = xlsxwriter.Workbook('parcerivi.xlsx')
# worksheet = workbook.add_worksheet()
# url = 'https://www.ivi.ru/movies/2020'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# quotes = soup.find('div', class_='nbl-slimPosterBlock__title').text
# worksheet.write(1, 1, quotes)
# print(quotes)
# workbook.close()
#
# # открываем новый файл на запись
# workbook = xlsxwriter.Workbook('parcerexample.xlsx')
#
# worksheet = workbook.add_worksheet()
#
# worksheet.write('A1', quotes)
#
# workbook.close()
# url = 'https://www.kinopoisk.ru/lists/navigator/?page=2&sort=popularity&quick_filters=yandex_plus_subscription&tab=online'# url страницы
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
#
# print(soup.encode('UTF-8'))
# # for n in range(50):
# #     quotes = soup.findAll('p', class_='selection-film-item-meta__name')[n].text
# #                         # worksheet.write(n, num, quotes)
#     print(quotes)
# #                 # print(num)
# # print(url)
# # workbook = xlsxwriter.Workbook('parcerscnd.xlsx')
# # worksheet = workbook.add_worksheet()
#
# for num in range(1, 10):
#         try:
#                 url = 'https://www.kinopoisk.ru/lists/navigator/?page=' + str(num) + '&sort=popularity&quick_filters=yandex_plus_subscription&tab=online'# url страницы
#                 r = requests.get(url)
#                 soup = BeautifulSoup(r.text, 'lxml')
#                 for n in range(50):
#                         quotes = soup.findAll('p', class_='selection-film-item-meta__name')[n].text
#                         # sub = soup.select_one(".online-block > a")
#                         print(quotes)
#                         # print(sub)
#                         # worksheet.write(n, num, quotes)
#
#                 # print(num)
#                 # print(url)
#                 # print(quotes)
#                 # print(sub)
#                 # time.sleep(10)
#         except Exception as ex:
#                 print('exeption', ex, num)
#                 continue
# # workbook.cl
# listOfsmth = []
# for x in range(1, 169):
#         listOfsmth.append(x)
# print(listOfsmth)
# for listOfsmth[0] in range(167):
#         print(listOfsmth[0])
#         listOfsmth.pop(0)
#         print(listOfsmth)

workbook = xlsxwriter.Workbook('subplusmoretv.xlsx')
worksheet = workbook.add_worksheet()
listOfExceptions = []
for x in range(1, 169):
    listOfExceptions.append(x)
for listOfExceptions in range(1, 168):
    try:
        url = 'https://www.kinopoisk.ru/lists/navigator/?page=' + listOfExceptions[0] + '&sort=popularity&quick_filters=yandex_plus_super_subscription&tab=online'  # url страницы
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        for n in range(50):
            quotes = soup.findAll('p', class_='selection-film-item-meta__name')[n].text
            worksheet.write(n, listOfExceptions[0], quotes)
        print(listOfExceptions[0])
        # print(url)
        time.sleep(10)
    except Exception as ex:
        print('exeption', ex, listOfExceptions[0])
        listOfExceptions.append(listOfExceptions[0])
        time.sleep(365)
        continue
workbook.close()
