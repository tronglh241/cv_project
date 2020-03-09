import cv2
import utils
import torch

from torchvision import transforms

from abstract.processor import Processor
from models.definitions.Net import Net


class NeuralNet(Processor):
    def __init__(self, image_size, weight_path, cuda):
        super(NeuralNet, self).__init__()
        self.image_size = image_size
        self.device = torch.device('cuda' if cuda else 'cpu')

        self.model = Net()
        self.model.load_state_dict(torch.load(utils.abs_path(weight_path), map_location='cpu'))
        self.model.eval()
        self.model.to(self.device)

    def preprocess(self, image, info):
        image = cv2.resize(image, dsize=self.image_size)
        image = transforms.ToTensor()(image)
        image = image.to(self.device)
        image = transforms.Normalize((0.1307,), (0.3081,))(image)
        image = image.unsqueeze(dim=0)

        return image, info

    def process(self, image, info):
        return self.model(image), info
        
    def postprocess(self, pred, info):
        pred = pred.squeeze(dim=0)
        return pred.argmax().item(), info