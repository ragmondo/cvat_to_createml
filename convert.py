import json
from typing import List
from typing import Any
from dataclasses import dataclass

from typing import List

import jsonpickle

# Example Usage
# jsonstring = json.load(open("annotations.json"))
from dataobjects import CVATImage, Annotation, Coordinates

y = CVATImage("9500c6ff-8902-4050-941f-888274bbf516.jpg", [Annotation("iraq", Coordinates(255, 250, 269, 500))])

dumps = jsonpickle.encode(y, unpicklable=False)
print(dumps)
print("----")

xxx = 123


example = """{
    "image": "9500c6ff-8902-4050-941f-888274bbf516.jpg",
    "annotations": [
        {
            "label": "iraq",
            "coordinates": {
                "x": 255,
                "y": 250,
                "width": 269,
                "height": 500
            }
        }
    ]
}"""

a1 = json.loads(example)
a2 = json.loads(dumps)
print(a1)
print(a2)
print(a1 ==a2)

"""  
<annotations>
<image id="1" name="220px-Holland_VC_f&amp;b.jpeg" subset="default" task_id="1" width="220" height="249">
    <box label="victoria-cross" occluded="0" source="manual" xtl="13.98" ytl="60.59" xbr="101.71" ybr="239.95" z_order="0">
    </box>
    <box label="victoria-cross" occluded="0" source="manual" xtl="118.89" ytl="63.30" xbr="205.11" ybr="238.45" z_order="0">
    </box>
  </image>
  </annotations>
  """

#  <box label="victoria-cross" occluded="0" source="manual" xtl="13.98" ytl="60.59" xbr="101.71" ybr="239.95" z_order="0">

# <box label="victoria-cross" occluded="0" source="manual" xtl="118.89" ytl="63.30" xbr="205.11" ybr="238.45" z_order="0">


# output = jsonpickle.encode(all_images, unpicklable=False, indent= 2)
#
# print(output)
#
# with open("out/annotations.json",'w') as f:
#     f.write(output)

from PIL import Image, ImageDraw

def nonsense(all_images):
    for i in all_images:
        image = Image.open("out/" + i.image)
        for annotation in i.annotations:
            x0 = annotation.coordinates.x
            y0 = annotation.coordinates.y
            width = annotation.coordinates.width
            height = annotation.coordinates.height
            x1 = x0 + width
            y1 = y0 + height

            shape = [(x0,y0), (x1,y1)]

            # creating new Image object

            draw = ImageDraw.Draw(image)
            try:
                draw.rectangle(shape, outline ="green")
            except ValueError:
                print("value error -skipping")

        image.show()


# {
#     "image": "76354872-fb1e-4118-9f66-9ffe1a92780d.jpg",
#     "annotations": [
#         {
#             "label": "victoria-cross",
#             "coordinates": {
#                 "x": 158,
#                 "y": 122,
#                 "width": 99,
#                 "height": 223
#             }
#         },
#         {
#             "label": "victoria-cross",
#             "coordinates": {
#                 "x": 53,
#                 "y": 127,
#                 "width": 97,
#                 "height": 232
#             }
#         }
#     ]
# },

    # my creation
    # {
    #     "image": "220px-Holland_VC_f&b.jpeg",
    #     "annotations": [
    #         {
    #             "label": "victoria-cross",
    #             "coordinates": {
    #                 "x": 13,
    #                 "y": 60,
    #                 "width": 88,
    #                 "height": 179
    #             }
    #         },
    #         {
    #             "label": "victoria-cross",
    #             "coordinates": {
    #                 "x": 118,
    #                 "y": 63,
    #                 "width": 87,
    #                 "height": 175
    #             }
    #         }
    #     ]
    # },



