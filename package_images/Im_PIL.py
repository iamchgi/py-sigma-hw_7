# ------------------------  Технології Computer Vision з python -------------------------------

"""
Переробив(сплогиатив): Григорій Чернолуцький
Цифрова обробка зображень: класичні алгоритми "сирої" обробки растрового зображення з пакетом  Pillow (PIL)
Джерела даних:
https://www.kaggle.com/datasets
https://www.sentinel-hub.com/
https://livingatlas2.arcgis.com/landsatexplorer/

Package         Version
--------------- -------
matplotlib      3.9.2
pillow          11.0.0

"""

from PIL import Image, ImageDraw
from matplotlib import pyplot as plt


# Клас, екземпляри якого будуть зберігати зображення
class ImageInfo:
    def __init__(self, file_name: str):
        self.image = Image.open(file_name)  # відкриття файлу зображення
        self.draw = ImageDraw.Draw(self.image)  # створення інструменту для малювання
        self.width = self.image.size[0]  # визначення ширини картинки
        self.height = self.image.size[1]  # визначення висоти картинки
        self.pix = self.image.load()  # отримання значень пікселів для картинки
        # pix[1, 1][1]: (x,y),(red, green, blue), де x,y — координати, а числові значення RGB - в межах 0-255 кожне.
        print("START_im", end=" ")
        self.show_first_pix()
        self.show_all()

    # Малювання зображення яке зберігається в екземплярі класу ImageInfo
    def show_all(self) -> None:
        plt.imshow(self.image)
        plt.show()

    # Інформація про перший піксель
    def show_first_pix(self) -> None:
        print("red=", self.pix[1, 1][0], "green=", self.pix[1, 1][1], "blue=", self.pix[1, 1][2])

    # Збереження зображення яке зберігається екземпляром класу ImageInfo в файл
    def save(self, file_name: str, file_type: str) -> None:
        self.image.save(file_name, file_type)

    # Руйнація інструменту малювання
    def destroy(self) -> None:
        del self.draw


# --------------------- відтінків сірого ----------------------
def shades_of_gray(file_name_start: str, file_name_stop: str) -> None:
    """
    :param file_name_start: Вхідний файл зображення для перетворення
    :param file_name_stop: Вихідний файл зміненого зображення
    :return:
    """
    image = ImageInfo(file_name_start)
    print('------- триває перетворення --------------')
    for i in range(image.width):
        for j in range(image.height):
            a = image.pix[i, j][0]
            b = image.pix[i, j][1]
            c = image.pix[i, j][2]
            s = (a + b + c) // 3  # усередненя пікселів
            image.draw.point((i, j), (s, s, s))

    image.show_all()
    print("STOP_im", end=" ")
    image.show_first_pix()
    image.save(file_name_stop, "JPEG")
    image.destroy()
    print(f'------- перетворення відтінків сірого завершене до файлу {file_name_stop} --------------')
    return


# ----------------------- негатив --------------------------
def negative(file_name_start: str, file_name_stop: str) -> None:
    """
       :param file_name_start: Вхідний файл зображення для перетворення
       :param file_name_stop: Вихідний файл зміненого зображення
       :return:
       """
    image = ImageInfo(file_name_start)
    print('------- триває перетворення --------------')
    for i in range(image.width):
        for j in range(image.height):
            a = image.pix[i, j][0]
            b = image.pix[i, j][1]
            c = image.pix[i, j][2]
            # Від кожного пікселя віднімається 256 - максимальне. значення для кольору
            image.draw.point((i, j), (255 - a, 255 - b, 255 - c))

    image.show_all()
    print("STOP_im", end=" ")
    image.show_first_pix()
    image.save(file_name_stop, "JPEG")
    image.destroy()
    print(f'------- перетворення негатив завершене до файлу {file_name_stop} --------------')
    return


# ---------------------- зміна яскравості  --------------------
def brightness_change(file_name_start: str, file_name_stop: str) -> None:
    """
       :param file_name_start: Вхідний файл зображення для перетворення
       :param file_name_stop: Вихідний файл зміненого зображення
       :return:
       """
    image = ImageInfo(file_name_start)
    print('введіть діапазон зміни яскравості: -100, +100')
    factor = int(input('factor:'))  # наприклад в діапазоні +100, -100
    print('------- триває перетворення --------------')
    for i in range(image.width):
        for j in range(image.height):
            a = image.pix[i, j][0] + factor  # додавання яскравості
            b = image.pix[i, j][1] + factor
            c = image.pix[i, j][2] + factor
            if (a < 0):
                a = 0
            if (b < 0):
                b = 0
            if (c < 0):
                c = 0
            if (a > 255):
                a = 255
            if (b > 255):
                b = 255
            if (c > 255):
                c = 255
            image.draw.point((i, j), (a, b, c))

    image.show_all()
    print("STOP_im", end=" ")
    image.show_first_pix()
    image.save(file_name_stop, "JPEG")
    image.destroy()
    print(f'------- перетворення зміна яскравості завершене до файлу {file_name_stop} --------------')
    return
