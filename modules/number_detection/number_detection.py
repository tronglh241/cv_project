from typing import Tuple

import cv2
import numpy as np

from abstract.stage import Stage

from .dto import Info


class NumberDetection(Stage):
    def preprocess(self, image_path: str) -> Tuple[np.ndarray, Info]:
        info = Info(image_path)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        return image, info

    def postprocess(self, number: int, info: Info) -> Tuple[Info]:
        info.number = number

        return info,
