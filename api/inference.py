import torch, torch.nn.functional as F
from models.cloud_monitor_model import CloudHealthNet
from api.schema import InputMetrics

model = CloudHealthNet(num_classes=2, input_dim=3)
model.load_state_dict(torch.load("model.pth", map_location="cpu"))
model.eval()


def predict_health(input: InputMetrics):
    x = torch.tensor(
        [[input.error_count, input.log_level_score, input.event_density]],
        dtype=torch.float,
    )
    with torch.no_grad():
        logits = model(x)
        probs = F.softmax(logits, dim=1)
        pred = torch.argmax(probs, dim=1).item()
    return {"prediction": pred, "confidence": probs[0][pred].item()}
