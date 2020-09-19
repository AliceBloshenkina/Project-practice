from os import listdir, rename
from os.path import isfile, join
import tkinter as tk
from PIL import ImageTk, Image
from PIL import Image, ImageDraw 
from os import remove

def __init__():
    global IMAGE_FOLDER, current, unclassified_images
    
    def next_img():
        global current
        try:
            current = next(unclassified_images)
        except StopIteration:
            root.quit()

        in_black(current)
        
        print(current)
        pil_img = Image.open(IMAGE_FOLDER+"\\"+current)
        width, height = pil_img.size
        max_height = 1000
        if height > max_height:
            resize_factor = max_height / height
            pil_img = pil_img.resize((int(width*resize_factor), int(height*resize_factor)), resample=Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(pil_img)
        img_label.img = img_tk
        img_label.config(image=img_label.img)

        return current, unclassified_images

    def positive(arg):
        rename(IMAGE_FOLDER+"/"+current, IMAGE_FOLDER+"/1_"+current)
        next_img()

    def negative(arg):
        global current
        rename(IMAGE_FOLDER + "/" + current, IMAGE_FOLDER + "/0_" + current)
        next_img()

    def in_black(current):
        image = Image.open(IMAGE_FOLDER+"\\"+current)  # Открываем изображение
        draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
        width = image.size[0]  # Определяем ширину
        height = image.size[1]  # Определяем высоту
        pix = image.load()  # Выгружаем значения пикселей

        for x in range(width):
            for y in range(height):
                r = pix[x, y][0] #узнаём значение красного цвета пикселя
                g = pix[x, y][1] #зелёного
                b = pix[x, y][2] #синего
                sr = (r + g + b) // 3 #среднее значение
                draw.point((x, y), (sr, sr, sr)) #рисуем пиксель

        remove(IMAGE_FOLDER+"\\"+current)

        image.save(IMAGE_FOLDER+"\\"+current) 
    
    IMAGE_FOLDER = "c:\\Users\\ALISA\\Desktop\\Вуз\\Проектная практика\\Мужчины"

    images = [f for f in listdir(IMAGE_FOLDER) if isfile(join(IMAGE_FOLDER, f))]
    unclassified_images = filter(lambda image: not (image.startswith("0_") or image.startswith("1_")), images)
    current = str(None)

    root = tk.Tk()

    img_label = tk.Label(root)
    img_label.pack()
    img_label.bind("<Button-1>", positive)
    img_label.bind("<Button-3>", negative)

    btn = tk.Button(root, text='Next image', command=next_img)

    next_img() # load first image

    root.mainloop()


    # if __name__ == "__main__":
