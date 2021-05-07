import cv2
import torch
import utils
import numpy as np

from ..dto import Info
from typing import cast, Tuple
from torchvision import transforms
from models.definitions.Net import Net
from abstract.processor import Processor


class NeuralNet(Processor):
    def __init__(self, image_size: Tuple[int, int], weight_path: str, device: str):
        super(NeuralNet, self).__init__()
        self.image_size = image_size
        self.device = device

        self.model = Net()
        self.model.load_state_dict(torch.load(utils.abs_path(weight_path), map_location='cpu'))
        self.model.eval()
        self.model.to(self.device)

    def preprocess(self, image: np.ndarray, info: Info) -> Tuple[torch.Tensor, Info]:
        image = cv2.resize(image, dsize=self.image_size)
        image: torch.Tensor = transforms.ToTensor()(image)
        image = image.to(self.device)
        image = transforms.Normalize((0.1307,), (0.3081,))(image)
        image = image.unsqueeze(dim=0)

        return image, info

    def process(self, image: torch.Tensor, info: Info) -> Tuple[torch.Tensor, Info]:
        return self.model(image), info

    def postprocess(self, pred: torch.Tensor, info: Info) -> Tuple[int, Info]:
        pred = pred.squeeze(dim=0)
        pred = cast(int, pred.argmax().item())
        return pred, info
