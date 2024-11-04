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
Порядок реалізації Блоку 2 структурної схеми рис.1.
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
схеми рис.1.
Рівень складності ІІ – 6 балів. Реалізувати завдання з реалізації на вибір Блоку 2, або
Блоку 3 структурної схеми рис.1.

Package Version
------- -------
pip 24.3.1

"""

import package_images.Im_PIL
from package_parsing import (
    SiteParsing
)
from package_cv import (
    SoftwareDeveloper,
    Profffesssor,
    Locksmith
)


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

def package_image_main_def() -> None:
    file_name_start = 'sentinel_2023.jpg'
    file_name_stop = "stop.jpg"
    file_name_filter = "stop_filter.jpg"

    print('оберіть тип перетворення!')
    print('0 - відтінки сірого')
    print('1 - серпія')
    print('2 - негатив')
    print('3 - зашумлення')
    print('4 - зміна яскравості')
    print('5 - монохромне зображення')
    print('6 - фільтр-векторизатор')
    mode = int(input('mode:'))
    if (mode == 0): package_images.Im_PIL.shades_of_gray(file_name_start, file_name_stop)
    if (mode == 1): package_images.Im_PIL.serpia(file_name_start, file_name_stop)
    if (mode == 2): package_images.Im_PIL.negative(file_name_start, file_name_stop)
    if (mode == 3): package_images.Im_PIL.noise(file_name_start, file_name_stop)
    if (mode == 4): package_images.Im_PIL.brightness_change(file_name_start, file_name_stop)
    if (mode == 5): package_images.Im_PIL.monochrome(file_name_start, file_name_stop)
    if (mode == 6): package_images.Im_PIL.contour_im(file_name_stop, file_name_filter)

    return


def package_parsing_main_def() -> None:
    site_parsing = SiteParsing()

    return


# --------------------------------- main module ----------------------------------------------
if __name__ == '__main__':
    # ------------------------  CV ----------------------------
    package_cv_main_def()
    # ------------------------ Приклад роботи з зображенням ----------------------------
    package_image_main_def()
    # ------------------------ Демонстрація парсингу сайтіка ----------------------------
    package_parsing_main_def()

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



'''
