# --------------------------- Homework_6.1  ------------------------------------
"""
Виконав: Григорій Чернолуцький
Homework_7
Завдання.
1. Cтворити проект python будь-яким способом, що реалізує архітектуру програмного
скрипта одного з блоків структурної схеми за власним вибором.
2. Створити віртуальне середовище - Virtual Environment.
сформуйте властивості у файлі requirements.txt;
встановіть пакет із файлу requirements.txt.
архів проекту надайте на перевірку
2. Створити віртуальне середовище - Virtual Environment.
сформуйте властивості у файлі requirements.txt;
встановіть пакет із файлу requirements.txt.
архів проекту надайте на перевірку.
*** додаткове завдання для самостійного опрацювання + 2 бали.
3. Зареєструйтесь на сайті https://github.com
створіть приватний (Private!!!) репозиторій з ім’ям lesson-4-9.
відповідно до інструкцій https://docs.github.com/en/get-started/quickstart/hello-world -
завантажте створений Вами проект до репозиторію Lesson-4-9.
Посилання на репозиторій додайте до архіву проекту.
Порядок реалізації Блоку 2 структурної схеми рис. 1.
1. Оберіть джерело даних дистанційного зондування Землі (ДЗЗ) з переліку:
https://www.kaggle.com/
https://paperswithcode.com/
https://www.sentinel-hub.com/
https://livingatlas2.arcgis.com/landsatexplorer/
https://www.bing.com/maps
https://unitar.org/maps/map/3525
https://mapcarta.com/Map
за власним вибором
або будь-яке цифрове зображення.
2. Оберіть район поверхні землі та цікаві об’єкти / об’єкт, наприклад: посівні
території; зелені насадження; вирубки лісів; стаціонарні об’єкти забудови; рухомі об’єкти
тощо.
3. Проведіть дослідження процесів цифрової обробки зображень з переліку скрипта
Im_PIL.py – щоб вибудовати послідовність, яка дозволяє отримати чіткій замкнутий контур
обраного об’єкту.
4. Для знайденої комбінації етапів цифрової обробки зображень проведіть
рефакторинг (редагування) програмного коду скрипта Im_PIL.py за принципами
архітектурної «чистоти» - стандарти РЕР, принципи SOLID.
Рівень складності І – 4 бали. Реалізувати завдання з реалізації Блоку 1, структурної
схеми рис. 1.
Рівень складності II – 6 балів. Реалізувати завдання з реалізації на вибір Блоку 2, або
Блоку 3 структурної схеми рис. 1.

Package Version
------- -------
pip 24.3.1

"""
import pandas as pd
import os
from package_images.Im_PIL import brightness_change, shades_of_gray, negative
from package_parsing import (
    parsing_site_bank_gav_ua
)
from package_cv import (
    SoftwareDeveloper,
    Profffesssor,
    Locksmith
)


#   Метод створення і заповнення трьох резюмує
def package_cv_main_def() -> None:
    software_developer = SoftwareDeveloper('Тарас Бульба', '1976', '48')
    software_developer.set_language(("Python", "Pascal", "Java", "VB", "PHP"))

    professor = Profffesssor('Василь Пупкін', '2000', '24')
    professor.set_teaching('10')
    professor.set_subjects(("history", "psychology", "microbiology", "genetics", "philosophy"))

    locksmith = Locksmith('Дід Панас', '1917', '107')
    locksmith.set_tools(('hammer', 'knife', 'screwdriver', 'pliers'))

    for vocation in (software_developer, professor, locksmith):
        vocation.draw()
        vocation.save()

    return


def package_image_main_def(source_file, destination_file) -> None:
    """
    :param source_file: Вихідне джерело зображення для перетворення
    :param destination_file:  Файл результату з перетвореним зображенням
    :return:
    """
    file_temp01 = 'temp01.jpg'
    file_temp02 = "temp02.jpg"
    print('перетворення!')
    print('відтінки сірого')
    shades_of_gray(source_file, file_temp01)
    print('негатив')
    negative(file_temp01, file_temp02)
    print('зміна яскравості')
    brightness_change(file_temp02, destination_file)
    os.remove(file_temp01)
    os.remove(file_temp02)
    return


def package_parsing_main_def() -> None:
    print("\nКурс НБУ")
    URL_TEMPLATE = "https://bank.gov.ua/ua/markets/exchangerates"

    df = pd.DataFrame(data=parsing_site_bank_gav_ua(URL_TEMPLATE))
    df.to_csv("output/exchange.csv")
    df.to_excel("output/exchange.xlsx")
    df.to_json("output/exchange.json")
    print("Дані збережені в файли")
    return


def main() -> None:
    # ------------------------  CV ----------------------------
    package_cv_main_def()
    # ------------------------ Приклад роботи з зображенням ----------------------------
    package_image_main_def('images/sphinx3.jpg', 'images/sphinx_r.jpg')
    # ------------------------ Демонстрація парсингу сайтика ----------------------------
    package_parsing_main_def()


# --------------------------------- main module ----------------------------------------------
if __name__ == '__main__':
    main()

''' 
РЕЗУЛЬТАТ

Software developer
 Ім'я, прізвище: Тарас Бульба
 Дата народження: 1976
 Вік: 48
 Мови програмування:
Python Pascal Java VB PHP  
------------------------ запис CV у файл "Тарас Бульба.txt" ----------------------
CV was saved successfully in file "Тарас Бульба.txt"
Writing file module finished its work with current file "Тарас Бульба.txt".

Профффесссор
 Ім'я, прізвище: Василь Пупкін
 Дата народження: 2000
 Вік: 24
 Викладацький стаж: 10
 Викладає таке от:
history psychology microbiology genetics philosophy  
------------------------ запис CV у файл "Василь Пупкін.txt" ----------------------
CV was saved successfully in file "Василь Пупкін.txt"
Writing file module finished its work with current file "Василь Пупкін.txt".

locksmith
 Ім'я, прізвище: Дід Панас
 Дата народження: 1917
 Вік: 107
 Має інструменти:
hammer knife screwdriver pliers  
------------------------ запис CV у файл "Дід Панас.txt" ----------------------
CV was saved successfully in file "Дід Панас.txt"
Writing file module finished its work with current file "Дід Панас.txt".

перетворення!
відтінки сірого
START_im red= 207 green= 184 blue= 134
------- триває перетворення --------------
STOP_im red= 175 green= 175 blue= 175
------- перетворення відтінків сірого завершене до файлу temp01.jpg --------------
негатив
START_im red= 175 green= 175 blue= 175
------- триває перетворення --------------
STOP_im red= 80 green= 80 blue= 80
------- перетворення негатив завершене до файлу temp02.jpg --------------
зміна яскравості
START_im red= 80 green= 80 blue= 80
введіть діапазон зміни яскравості: -100, +100
factor:50
------- триває перетворення --------------
STOP_im red= 130 green= 130 blue= 130
------- перетворення зміна яскравості завершене до файлу sphinx_r.jpg --------------

Курс НБУ
['036', '944', '933', '975', '410', '344', '208']
['AUD', 'AZN', 'BYN', 'BGN', 'KRW', 'HKD', 'DKK']
['1', '1', '1', '1', '100', '1', '1']
[' Австралійський долар ', ' Азербайджанський манат ', ' Білоруський рубль ', ' Болгарський лев ', ' Вона ', ' Гонконгівський долар ', ' Данська крона ']
['27,2243', '24,3960', '15,0684', '22,6710', '2,9572', '5,3312', '5,9457']

'''
