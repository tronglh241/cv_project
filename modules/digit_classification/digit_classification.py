from typing import Tuple

from abstract.stage import Stage
from dto.info import Info


class DigitClassification(Stage):
    def preprocess(self, info: Info) -> Tuple[Info]:
        return info,

    def postprocess(self, info: Info) -> Tuple[Info]:
        return info,
