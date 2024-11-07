# ------------------ HTTP: для парсингу сайтів ----------------------------
"""

Приклад
парсингу сайтів із збереженням інформації до файлів різного формату
df.to_csv("output.csv")
df.to_excel("output.xlsx")
df.to_json("output.json")

Package                      Version
---------------------------- -----------
pip                          23.1
requests                     2.28.2
beautifulsoup4               4.12.3

"""

import requests
from bs4 import BeautifulSoup as bs


class SiteParsing:
    def __init__(self):
        pass


def parsing_site_work_ua (URL_TEMPLATE):
    """
    site parsing python
    web scraping / site scraping python
    Data scraping - швидше очищення та підготовка даних
    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html

    :param URL_TEMPLATE: URL Site work.ua
    :return: class 'dict'
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    '''
    Зміни в аргументі для методу get: headers=headers - МИ відрекомендувались звичайним браузером при зверненні до серверу.
    '''
    r = requests.get(URL_TEMPLATE, headers=headers)
    result_list = {'href': [], 'title': [], 'about': []}
#    print(r.status_code)
 #   print(r.text)
    soup = bs(r.text, "html.parser")
    vacancies_names = soup.find_all('div', class_="mb-lg")
    vacancies_info = soup.find_all('p', class_='ellipsis')
    constant = 5 # для балансування даних
    i = 0
    for name in vacancies_names:
        i = i + 1
        if (i < (len(vacancies_names) - constant)):
 #           print(name.a['title'])
            result_list['title'].append(name.a['title'])
  #          print('https://www.work.ua' + name.a['href'])
            result_list['href'].append('https://www.work.ua' + name.a['href'])
    i = 0
    for info in vacancies_info:
        i = i + 1
        if (i < (len(vacancies_names) - constant)):
 #           print(info.text)
            result_list['about'].append(info.text)

    print(result_list['title'])
    print(result_list['href'])
    print(result_list['about'])
    return result_list
