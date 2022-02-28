import requests
import time
import xlsxwriter
from bs4 import BeautifulSoup
workbook = xlsxwriter.Workbook('subplussuper.xlsx')
worksheet = workbook.add_worksheet()
listOfExceptions = []

for num in range(1, 100):
        try:
                url = 'https://www.kinopoisk.ru/lists/navigator/?page=' + str(num) + '&sort=popularity&quick_filters=yandex_plus_super_subscription&tab=online'# url страницы
                r = requests.get(url)
                soup = BeautifulSoup(r.text, 'lxml')
                for n in range(50):
                        quotes = soup.findAll('p', class_='selection-film-item-meta__name')[n].text
                        worksheet.write(n, num, quotes)

                print(num)
                # print(url)
                # time.sleep(10)
        except Exception as ex:
                print('exeption', ex, num)
                listOfExceptions.append(num)
                # time.sleep(365)
                continue
print(listOfExceptions)

while len(listOfExceptions) != 0:
        for num in listOfExceptions:
                try:
                        url = 'https://www.kinopoisk.ru/lists/navigator/?page=' + str(
                                num) + '&sort=popularity&quick_filters=yandex_plus_super_subscription&tab=online'  # url страницы
                        r = requests.get(url)
                        soup = BeautifulSoup(r.text, 'lxml')
                        for n in range(50):
                                quotes = soup.findAll('p', class_='selection-film-item-meta__name')[n].text
                                worksheet.write(n, num, quotes)
                        listOfExceptions.pop(0)
                        print(num)
                        # print(url)
                        # time.sleep(10)
                except Exception as ex:
                        print('exeption', ex, num)
                        listOfExceptions.append(num)
                        # time.sleep(365)
                        continue
workbook.close()
# root.mainloop()













# for i in range(0, listOfExceptions.count()):
#         print(listOfExceptions[i])

# url = 'https://www.kinopoisk.ru/lists/navigator/?sort=popularity&quick_filters=available_online&tab=online'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# quotes = soup.find_all('p', class_='selection-film-item-meta__name')
# print(quotes)
#
