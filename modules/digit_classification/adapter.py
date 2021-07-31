from typing import Tuple

import cv2
import numpy as np

from abstract.adapter import InAdapter as _InAdapter
from abstract.adapter import OutAdapter as _OutAdapter
from dto.info import Info


class InAdapter(_InAdapter):
    def convert(self, stage_input: Tuple[Info]) -> Tuple[np.ndarray]:
        info = stage_input[0]
        image = cv2.imread(info.image_path, cv2.IMREAD_GRAYSCALE)
        return image,


class OutAdapter(_OutAdapter):
    def convert(self, stage_input: Tuple, stage_output: Tuple) -> Tuple[Info]:
        info = stage_input[0]
        number = stage_output[0]
        info.number = number
        return info,
