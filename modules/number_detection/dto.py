from abstract.dto import DTO


class Info(DTO):
    def __init__(self, image_path: str = None, number: int = None):
        super(Info, self).__init__()
        self.image_path = image_path
        self.number = number
