
from PIL import Image, ImageDraw, ImageFont

from convert import CVATImage

import jsonpickle

def display_image_with_bb(folder, cvat_image: CVATImage):
    try:
        image = Image.open(folder + cvat_image.image)
        print(cvat_image)
        print()
        draw = ImageDraw.Draw(image)

        for i, annotation in enumerate(cvat_image.annotations):
            x0 = annotation.coordinates.x
            y0 = annotation.coordinates.y
            width = annotation.coordinates.width
            height = annotation.coordinates.height

            x_centre = x0 - width / 2
            y_centre = y0 - height / 2

            x1 = x0 + width / 2
            y1 = y0 + height / 2
            shape = [(x_centre, y_centre), (x1,y1)]

            textfont = ImageFont.truetype("Keyboard.ttf", 20)
            anno_text = f"{annotation.label} x {x0} y {y0}, width {width}, height {height}"
            draw.text((i + 5, 30*(i+4) + 5), anno_text, font=textfont, fill = "#000")
            try:
                draw.rectangle(shape, outline ="green", width=5)
            except ValueError:
                print("value error -skipping")


        textfont = ImageFont.truetype("Keyboard.ttf", 20)
        draw.text((5,5), cvat_image.image, font=textfont)
        draw.text((5,35), str(image.size), font=textfont)

        image.show()
    except FileNotFoundError as e:
        print(f"Couldn't find {e}")
