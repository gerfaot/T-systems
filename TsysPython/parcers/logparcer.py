import xlsxwriter
import requests
from bs4 import BeautifulSoup
import pandas as pd
excel_data_df = pd.read_excel('Test.xlsx', sheet_name='Лист1')
container = excel_data_df['№ контейнера'].tolist()
i = 1
workbook = xlsxwriter.Workbook('next.xlsx')
worksheet = workbook.add_worksheet()
exep = 'problem'
for item in container:
    try:
        response = requests.get('http://www.cma-cgm.com/ebusiness/tracking/search?SearchBy=Container&Reference=' + item)
        soup = BeautifulSoup(response.text, "lxml")
        worksheet.write(i, 4, item)
        worksheet.write(i, 5, soup.findAll("td", class_="is-header js-openrow")[-1].text.strip())
        worksheet.write(i, 6, soup.findAll("td", class_="is-headerdata js-openrow")[-1].text.strip())
        worksheet.write(i, 7, soup.findAll("td", attrs={'data-label': 'Vessel'})[-1].text.strip())
        print(i)
        i += 1
        print(soup.findAll("td", class_="is-header js-openrow")[-1].text.strip())
        print(soup.findAll("td", class_="is-headerdata js-openrow")[-1].text.strip())
        print(soup.findAll("td", attrs={'data-label': 'Vessel'})[-1].text.strip())
    except Exception as ex:
        print('exeption', ex)
        worksheet.write(i, 4, item)
        worksheet.write(i, 5, exep)
        print(i)
        i += 1
        continue
workbook.close()
