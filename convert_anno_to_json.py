import os
import sys

import jsonpickle
import shutil
from dataobjects import CVATImage
from validate_directory import validate_directory_xml

def tidy_dir(folder):
    for d in [x for x in os.listdir(folder) if os.path.isdir(folder + "/" + x)]:
        shutil.rmtree(folder + "/" + d)

if __name__ == "__main__":
    # Takes a directory, reads annotations.xml, spits out annotations.json which is createml compatible.
    # dirname = sys.argv[1]
    dirname = "data/george-vc-3"

    cvat_images = validate_directory_xml(dirname)

    for i in cvat_images:
        i.auto_rename(dirname)

    with open(f"{dirname}/annotations.json","w") as anno_json_file:
        anno_json_file.write(jsonpickle.encode(cvat_images, unpicklable=False))

    ## Tidy / Remove all other folders

    tidy_dir(dirname)





