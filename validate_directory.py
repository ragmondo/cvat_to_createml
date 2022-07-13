
import json
import jsonpickle

from dataobjects import CVATImage, Annotation, Coordinates
from imageutils import display_image_with_bb

import xml.etree.ElementTree as ET

def validate_directory_json(directory):
    cvats = []

    with open(directory + "/annotations.json", "r") as anno_filename:
        images = json.load(anno_filename)
        # print(images)
        for i in images:
            # print(i)

            annotations = []
            for a in i.get("annotations"):
                coords = a.get("coordinates")
                anno = Annotation(a.get("label"), Coordinates(coords.get("x"), coords.get("y"), coords.get("width"), coords.get("height")))
                annotations.append(anno)
                cvat_image = CVATImage(i.get("image"), annotations)

            cvats.append(cvat_image)
    return cvats

def validate_directory_xml(directory, all_images = True, filter_subset = "default"):

    tree = ET.parse(f"{directory}/annotations.xml")
    root = tree.getroot()

    all_images = []

    for image in root.iter("image"):
        print(image)

        if image.get("subset") == filter_subset:

            annotations = []
            for b in image.iter("box"):
                x_min = int(float(b.get("xtl")))
                y_min = int(float(b.get("ytl")))
                x_max = int(float(b.get("xbr")))
                y_max = int(float(b.get("ybr")))
                height = y_max - y_min
                width = x_max - x_min
                x_centre = (x_min + x_max) / 2
                y_centre = (y_min + y_max) / 2
                # print(width, height)
                annotation = Annotation(b.get("label"), Coordinates(int(x_centre), int(y_centre), int(width), int(height)))
                annotations.append(annotation)

            cvat_image = CVATImage(image.get("name"), annotations)

            # print(cvat_image)
            # print(jsonpickle.encode(cvat_image, unpicklable=False))
            if annotations or all_images:
                all_images.append(cvat_image)
        else:
            print(f"Skipping as not subset match for {filter_subset}")

    return all_images

if __name__ == "__main__":

    json_folder = "data/vc-test"
    cvats1 = validate_directory_json(json_folder)

    for c in cvats1[0:10]:
        display_image_with_bb(json_folder+"/", c)
    #
    # folder = "out"
    #
    # cvats2 = list(filter(lambda x: (len(x.annotations)), validate_directory_xml(folder, all_images=False)))
    #
    # for c in cvats2:
    #     display_image_with_bb(folder+"/", c)
