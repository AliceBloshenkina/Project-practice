from PIL import Image, ImageDraw 
from os import remove
from urllib import request
from urllib.request import urlretrieve
from os import rename, remove
import itertools

def __init__(photos, url_img):
    for i in range(len(photos)): # download the photos to directory
        img = photos[i]
        nomber = str(i+1)
        urlretrieve(img, url_img)
        rename(url_img, url_img+"_"+nomber+".jpg")

def in_black(photos, url_img):

    for i in range(photos):
        nomber = str(i+1)
        image = Image.open(url_img+'_'+nomber+'.jpg')  
        draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
        width = image.size[0]  
        height = image.size[1]  
        pix = image.load()  # Выгружаем значения пикселей

        for x in range(width):
            for y in range(height):
                r = pix[x, y][0] #узнаём значение красного цвета пикселя
                g = pix[x, y][1] #зелёного
                b = pix[x, y][2] #синего
                sr = (r + g + b) // 3 #среднее значение
                draw.point((x, y), (sr, sr, sr)) #рисуем пиксель

        remove(url_img+"_"+nomber+".jpg")

        image.save(url_img+"_"+nomber+".jpg") 

    # for i in range(len(user.photos)): # removes photos from directory
    #     img = user.photos[i]
    #     nomber = str(i+1)
    #     remove("c:\\Users\\ALISA\\Desktop\\Вуз\\Проектная практика\\Фото\\img_person_"+nomber+".jpg")