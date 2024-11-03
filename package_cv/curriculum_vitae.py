# --------------------------- Homework_6.1  ------------------------------------
"""
Виконав: Григорій Чернолуцький
Модуль роботи з "CV":


Package Version
------- -------
pip 23.2.1

"""


# Друк на консоль вмісту змінної 'tuple'
def tuple_draw(kortezh) -> None:
    for item in kortezh:
        print(item, end=' ')
    print(" ")


# Батьківський клас  'Curriculum Vitae'
class CurriculumVitae:
    def __init__(self, name, birth, age):
        self.own_cv = dict({'name': name, 'birth': birth, 'age': age})

    # Друк на консоль вмісту словника з CV
    def draw(self) -> None:
        print(f" Ім'я, прізвище: {self.own_cv['name']}")
        print(f" Дата народження: {self.own_cv['birth']}")
        print(f" Вік: {self.own_cv['age']}")


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


# Збереження у файл даних типу строки
def save_cv_to_file(file_name: str, data: tuple) -> None:
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

    # ------------------------ запис CV у файли ----------------------------
def save_cv(cv :dict) -> None:
    file_types = ('txt', 'csv', 'dict')
    for file_type in file_types:
        current_file_name = cv['name'] + "." + file_type
        current_data = generate_cv_file_data(cv, file_type)
        save_cv_to_file(current_file_name, current_data)
    return