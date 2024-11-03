# ------------------------  Технології Computer Vision з python -------------------------------

'''
Цифрова обробка зображень: ласичні алгоритми "сирої" обробки растрового зображення з апакетом  Pillow (PIL)
Джерела даних:
https://www.kaggle.com/datasets
https://www.sentinel-hub.com/
https://livingatlas2.arcgis.com/landsatexplorer/

Package         Version
--------------- -------
matplotlib      3.8.2
pillow          10.2.0

'''


import random
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN)


# --------------------- зчитування файлу зображення ----------------------
def image_read(file_name: str) -> None:

	image = Image.open(file_name)  # відкриття файлу зображення
	draw = ImageDraw.Draw(image)  # створення інструменту для малювання
	width = image.size[0]   # визначення ширини картинки
	height = image.size[1]  # визначення висоти картинки
	pix = image.load()  # отримання значень пікселей для картинки
	# pix[1, 1][1]: (x,y),(red, green, blue), де x,y — координати, а числовые значения RGB - в межах 0-255 кожне.
	print("START_im", "red=", pix[1, 1][0], "green=", pix[1, 1][1], "blue=", pix[1, 1][2])
	plt.imshow(image)
	plt.show()
	image_info = {"image_file": image, "image_draw": draw, "image_width": width, "image_height": height, "image_pix": pix}

	return image_info


# --------------------- відтінкі сірого ----------------------
def shades_of_gray(file_name_start: str, file_name_stop: str) -> None:

	image_info = image_read(file_name_start)
	image = image_info["image_file"]
	draw = image_info["image_draw"]
	width = image_info["image_width"]
	height = image_info["image_height"]
	pix = image_info["image_pix"]

	print('------- триває перетворення --------------')

	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3  # усередненя пікселів
			draw.point((i, j), (S, S, S))

	plt.imshow(image)
	plt.show()
	print("STOP_im", "red=", pix[1, 1][0], "green=", pix[1, 1][1], "blue=", pix[1, 1][2])
	image.save(file_name_stop, "JPEG")
	del draw
	print('------- перетворення завершене до файлу stop.jpg --------------')

	return


# ------------------------- серпія  --------------------------
def serpia(file_name_start: str, file_name_stop: str) -> None:

	image_info = image_read(file_name_start)
	image = image_info["image_file"]
	draw = image_info["image_draw"]
	width = image_info["image_width"]
	height = image_info["image_height"]
	pix = image_info["image_pix"]

	print('------- ведіть коефіціент серпії --------------')
	depth = int(input('depth:'))
	print('------- триває перетворення --------------')
	for i in range(width):
		for j in range(height):  # підрахунок середнього значення кольорової гами - перетворення з коефіціентом
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3
			a = S + depth * 2
			b = S + depth
			c = S
			if (a > 255):
				a = 255
			if (b > 255):
				b = 255
			if (c > 255):
				c = 255
			draw.point((i, j), (a, b, c))

	plt.imshow(image)
	plt.show()
	print("STOP_im", "red=", pix[1, 1][0], "green=", pix[1, 1][1], "blue=", pix[1, 1][2])
	image.save(file_name_stop, "JPEG")
	del draw
	print('------- перетворення завершене до файлу stop.jpg --------------')

	return

# ----------------------- негатив --------------------------
def negative(file_name_start: str, file_name_stop: str) -> None:

	image_info = image_read(file_name_start)
	image = image_info["image_file"]
	draw = image_info["image_draw"]
	width = image_info["image_width"]
	height = image_info["image_height"]
	pix = image_info["image_pix"]

	print('------- триває перетворення --------------')
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			# від кожного пікселя віднімається 256 - макс. значення для кольору
			draw.point((i, j), (255 - a, 255 - b, 255 - c))

	plt.imshow(image)
	plt.show()
	print("STOP_im", "red=", pix[1, 1][0], "green=", pix[1, 1][1], "blue=", pix[1, 1][2])
	image.save(file_name_stop, "JPEG")
	del draw
	print('------- перетворення завершене до файлу stop.jpg --------------')

	return

# ----------------------- зашумлення ------------------------
def noise(file_name_start: str, file_name_stop: str) -> None:

	image_info = image_read(file_name_start)
	image = image_info["image_file"]
	draw = image_info["image_draw"]
	width = image_info["image_width"]
	height = image_info["image_height"]
	pix = image_info["image_pix"]

	print('------- введіть коефіціент шуму --------------')
	factor = int(input('factor:'))
	print('------- триває перетворення --------------')
	for i in range(width):
		for j in range(height):
			rand = random.randint(-factor, factor)
			a = pix[i, j][0] + rand  # додавання рандомного числа
			b = pix[i, j][1] + rand
			c = pix[i, j][2] + rand
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
			draw.point((i, j), (a, b, c))

	plt.imshow(image)
	plt.show()
	print("STOP_im", "red=", pix[1, 1][0], "green=", pix[1, 1][1], "blue=", pix[1, 1][2])
	image.save(file_name_stop, "JPEG")
	del draw
	print('------- перетворення завершене до файлу stop.jpg --------------')

	return

# ---------------------- зміна яскравості  --------------------
def brightness_change(file_name_start: str, file_name_stop: str) -> None:

	image_info = image_read(file_name_start)
	image = image_info["image_file"]
	draw = image_info["image_draw"]
	width = image_info["image_width"]
	height = image_info["image_height"]
	pix = image_info["image_pix"]

	print('введіть діапазон зміни яскравості: -100, +100')
	factor = int(input('factor:'))  # наприклад в діапазоні +100, -100
	print('------- триває перетворення --------------')
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0] + factor  # одавання яскравості
			b = pix[i, j][1] + factor
			c = pix[i, j][2] + factor
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
			draw.point((i, j), (a, b, c))

	plt.imshow(image)
	plt.show()
	print("STOP_im", "red=", pix[1, 1][0], "green=", pix[1, 1][1], "blue=", pix[1, 1][2])
	image.save(file_name_stop, "JPEG")
	del draw
	print('------- перетворення завершене до файлу stop.jpg --------------')

	return

# --------------------------- монохромне зображення ------------------------
def monochrome(file_name_start: str, file_name_stop: str) -> None:

	image_info = image_read(file_name_start)
	image = image_info["image_file"]
	draw = image_info["image_draw"]
	width = image_info["image_width"]
	height = image_info["image_height"]
	pix = image_info["image_pix"]

	print('------ введіть коефіціент розрізнення, в діапазоні 50-100 ----------')
	factor = int(input('factor:'))
	print('------- триває перетворення --------------')
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = a + b + c
			if (S > (((255 + factor) // 2) * 3)):  # рішення до якого з 2 кольорів поточне значення кольору ближче
				a, b, c = 255, 255, 255
			else:
				a, b, c = 0, 0, 0
			draw.point((i, j), (a, b, c))

	plt.imshow(image)
	plt.show()
	print("STOP_im", "red=", pix[1, 1][0], "green=", pix[1, 1][1], "blue=", pix[1, 1][2])
	image.save(file_name_stop, "JPEG")
	del draw
	print('------- перетворення завершене до файлу stop.jpg --------------')

	return

# ------------------ фільтрація - векторизація зображення ------------------------
def contour_im(file_name_start: str, file_name_stop: str) -> None:

	'''

	:param file_name_start: вхідне зображення
	:param file_name_stop: вихідне зображення
	:return: None

	# pillow 9.3.0
	# https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html
	# BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
	# EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN


	'''

	image_info = image_read(file_name_start)
	image = image_info["image_file"]
	draw = image_info["image_draw"]
	width = image_info["image_width"]
	height = image_info["image_height"]
	pix = image_info["image_pix"]

	# -----------  фільтрація: покращення якості, ідентифікація ---------------
	image_filter = image.filter(CONTOUR)
	# image_filter = image.filter(BLUR)
	# image_filter = image.filter(DETAIL)

	plt.imshow(image_filter)
	plt.show()
	pix = image_filter.load()  # отримання значень пікселей для картинки
	print("STOP_im", "red=", pix[1, 1][0], "green=", pix[1, 1][1], "blue=", pix[1, 1][2])
	image_filter.save(file_name_stop, "JPEG")
	del draw
	print('------- перетворення завершене до файлу stop.jpg --------------')

	return
