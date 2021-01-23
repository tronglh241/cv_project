import cv2

from abstract.dao import DAO
from abstract.stage import Stage


class NumberDetection(Stage):
    def preprocess(self, image_path):
        info = Info(image_path)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        return image, info

    def postprocess(self, number, info):
        info.number = number

        return info,


class Info(DAO):
    def __init__(self, image_path=None, number=None):
        super(Info, self).__init__()
        self.image_path = image_path
        self.number = number
