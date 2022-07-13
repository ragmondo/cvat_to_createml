from PIL import Image, ImageDraw

image = Image.open("data/cvat_for_images/images/0_ROYAL-Investitures-14152_101.jpeg")


# <box label="conspicuous-gallantry-cross" occluded="0" source="manual" xtl="138.69" ytl="251.53" xbr="207.11" ybr="374.28" z_order="0">

x0 = 138
y0 = 251
# x1 = 207
# y1 = 374

width = 69
height = 123

x1 = x0 + width
y1 = y0 + height

shape = [(x0,y0), (x1,y1)]

# creating new Image object

draw = ImageDraw.Draw(image)

draw.rectangle(shape, outline ="white")


image.show()