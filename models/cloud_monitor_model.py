import torch.nn as nn
from torchvision import models


class CloudHealthNet(nn.Module):
    def __init__(self, num_classes=2, input_dim=3):
        super(CloudHealthNet, self).__init__()
        # Small FC network instead of ResNet for tabular logs
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(64, num_classes),
        )

    def forward(self, x):
        return self.fc(x)
