from typing import Tuple, cast

import cv2
import numpy as np
import torch
from torchvision import transforms

from abstract.processor import Processor
from models.definitions.Net import Net
from utils.common import abs_path


class NeuralNet(Processor):
    def __init__(self, image_size: Tuple[int, int], weight_path: str, device: str):
        super(NeuralNet, self).__init__()
        self.image_size = image_size
        self.device = device

        self.model = Net()
        self.model.load_state_dict(torch.load(abs_path(weight_path), map_location='cpu'))
        self.model.eval()
        self.model.to(self.device)

    def preprocess(self, image: np.ndarray) -> Tuple[torch.Tensor]:
        image = cv2.resize(image, dsize=self.image_size)
        image: torch.Tensor = transforms.ToTensor()(image)
        image = image.to(self.device)
        image = transforms.Normalize((0.1307,), (0.3081,))(image)
        image = image.unsqueeze(dim=0)

        return image,

    def process(self, image: torch.Tensor) -> Tuple[torch.Tensor]:
        return self.model(image),

    def postprocess(self, pred: torch.Tensor) -> Tuple[int]:
        pred = pred.squeeze(dim=0)
        pred = cast(int, pred.argmax().item())
        return pred,
