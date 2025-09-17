import torch, torch.nn as nn, torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import pandas as pd, numpy as np
from models.cloud_monitor_model import CloudHealthNet


class LogDataset(Dataset):
    def __init__(self, csv_file):
        df = pd.read_csv(csv_file)
        self.X = df[["error_count", "log_level_score", "event_density"]].values.astype(
            np.float32
        )
        self.y = df["anomaly"].values.astype(np.int64)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]


def train():
    dataset = LogDataset("data/preprocessed_logs.csv")
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
    model = CloudHealthNet(num_classes=2, input_dim=3)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    for epoch in range(5):
        for X_batch, y_batch in dataloader:
            outputs = model(torch.tensor(X_batch))
            loss = criterion(outputs, torch.tensor(y_batch))
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")
    torch.save(model.state_dict(), "model.pth")


if __name__ == "__main__":
    train()
