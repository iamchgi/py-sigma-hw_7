# --------------------------- Homework_6.1  ------------------------------------
"""
Виконав: Григорій Чернолуцький
Модуль роботи з "CV":


Package Version
------- -------
pip 23.2.1

"""
from matplotlib.pyplot import title


# Друк на консоль вмісту змінної 'tuple'
def tuple_draw(kortezh) -> None:
    for item in kortezh:
        print(item, end=' ')
    print(" ")


# Перетворення даних типу словник в формат текст , csv, текст-словник
def generate_cv_file_data(cv: 'CurriculumVitae') -> tuple:
    """
    :param cv: Заповнене резезюме
    :return: Згенеровані дані для збереження в файл
    """
    result = list()
    for key, value in cv.own_cv.items():
        result.append(f'{key} : {value}')
    return tuple(result)


# Збереження у файл даних типу строки
def save_txt_to_file(file_name: str, data: tuple) -> None:
    """
    :param file_name: ім'я файлу у який зберігаємо CV
    :param data: дані для зберігання у файл
    :return: None
    """
    try:
        print(f'------------------------ запис CV у файл \"{file_name}\" ----------------------')
        with open(file_name, "w", encoding="UTF-8") as file:
            for line in data:
                file.write(line + "\n")
    except PermissionError:
        print("Sorry, you have no access to this file")
    except Exception as error:
        print(f"It looks like something has happened. This is {error}")
    else:
        print(f"CV was saved successfully in file \"{file_name}\"")
    finally:
        print(f"Writing file module finished its work with current file \"{file_name}\".\n")


# ------------------------ генерація процесу запису у файл ----------------------------
def save_to_file(cv: 'CurriculumVitae') -> None:
    """

    :param cv: об'єкт класу, або об'єкт нащядка класу, "CurriculumVitae" який зберігати будемо
    :return: None
    """
    current_file_name = cv.own_cv['name'] + '.txt'
    current_data = generate_cv_file_data(cv)
    save_txt_to_file(current_file_name, current_data)


# Батьківський клас  'Curriculum Vitae'
class CurriculumVitae:
    def __init__(self, name, birth, age):
        self.own_cv = dict({'name': name, 'birth': birth, 'age': age})

    # Друк на консоль вмісту словника з CV
    def draw(self) -> None:
        print(f" Ім'я, прізвище: {self.own_cv['name']}")
        print(f" Дата народження: {self.own_cv['birth']}")
        print(f" Вік: {self.own_cv['age']}")

    def save(self):
        pass


# клас 'Професор' нащадок батьківського класу 'Curriculum Vitae'
class Profffesssor(CurriculumVitae):
    title = "Профффесссор"

    def __init__(self, name, birth, age):
        super().__init__(name, birth, age)

    def set_teaching(self, teaching_time):
        self.own_cv.update({'teaching_time': teaching_time})

    def set_subjects(self, subjects):
        self.own_cv.update({'subjects': subjects})

    def draw(self):
        print(self.title)
        super().draw()
        print(f" Викладацький стаж: {self.own_cv['teaching_time']}")
        print(f" Викладає таке от:")
        tuple_draw(self.own_cv['subjects'])

    def save(self):
        save_to_file(self)


# клас 'Розробник' нащадок батьківського класу 'Curriculum Vitae'
class SoftwareDeveloper(CurriculumVitae):
    title = "Software developer"

    def __init__(self, name, birth, age):
        super().__init__(name, birth, age)

    def set_language(self, languages):
        self.own_cv.update({'languages': languages})

    def draw(self):
        print(self.title)
        super().draw()
        print(f" Мови програмування:")
        tuple_draw(self.own_cv['languages'])

    def save(self):
        save_to_file(self)


# клас 'Слюсар' нащадок батьківського класу 'Curriculum Vitae'
class Locksmith(CurriculumVitae):
    title = "locksmith"

    def __init__(self, name, birth, age):
        super().__init__(name, birth, age)

    def set_tools(self, tools):
        self.own_cv.update({'tools': tools})

    def draw(self) -> None:
        print(self.title)
        super().draw()
        print(f" Має інструменти:")
        tuple_draw(self.own_cv['tools'])

    def save(self):
        save_to_file(self)
