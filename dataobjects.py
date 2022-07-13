from typing import List

import uuid
import pathlib
import os


class Coordinates:
    x: int
    y: int
    width: int
    height: int

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"x: {self.x} y:{self.y} width:{self.width} height:{self.height}"


class Annotation:
    label: str
    coordinates: Coordinates

    def __init__(self, label: str, coordinates: Coordinates) -> None:
        self.label = label
        self.coordinates = coordinates

    def __str__(self):
        return f"<{self.label}> [{self.coordinates}]"

class CVATImage:
    image: str
    annotations: List[Annotation]

    def auto_rename(self, folder):
        old = self.image
        suffix = pathlib.Path(self.image).suffix
        if suffix == ".jpeg":
            suffix = ".jpg"
        id = uuid.uuid4()
        self.image = f"{id}{suffix}"
        os.rename(f"{folder}/images/default/{old}",f"{folder}/{self.image}")
        return self

    def __init__(self, image: str, annotations: List[Annotation]) -> None:
        self.image = image
        self.annotations = annotations

    def __str__(self):
        return f"{self.image} : \n" + "\n".join([f"--> {x}" for x in self.annotations])
