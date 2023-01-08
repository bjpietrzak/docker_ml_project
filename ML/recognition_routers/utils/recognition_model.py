import torch
import os


class Model:
    DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    def __init__(self, weights: str):
        self.weights = weights
        self.model = self._start_model()

    def _start_model(self):
        model = torch.hub.load('ultralytics/yolov5',
                               'custom',
                               self.weights)
        model.eval()
        if self.DEVICE == 'cuda':
            model.cuda()
        return model
    
    @torch.no_grad()
    def __call__(self, img):
        return self.model(img).pred

model = Model('recognition_routers/utils/crowdhuman_yolov5m.pt')