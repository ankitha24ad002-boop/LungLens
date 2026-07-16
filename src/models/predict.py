import os
import json
from PIL import Image

import torch
import torch.nn as nn
from torchvision import models, transforms

# -----------------------------
# Device
# -----------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# -----------------------------
# Model paths
# -----------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

MODEL_PATH = os.path.join(BASE_DIR, "models", "best_model.pth")
LABEL_MAP_PATH = os.path.join(BASE_DIR, "models", "label_map.json")

# -----------------------------
# Load Model
# -----------------------------
model = models.resnet18(weights=None)

model.fc = nn.Linear(model.fc.in_features, 2)

model.load_state_dict(torch.load(MODEL_PATH, map_location=device))

model.to(device)
model.eval()

# -----------------------------
# Load Label Map
# -----------------------------
with open(LABEL_MAP_PATH, "r") as f:
    label_map = json.load(f)

# -----------------------------
# Image Transform
# -----------------------------
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# -----------------------------
# Prediction Function
# -----------------------------
def predict_image(image_path):

    image = Image.open(image_path).convert("RGB")

    image = transform(image)

    image = image.unsqueeze(0).to(device)

    with torch.no_grad():

        outputs = model(image)

        probabilities = torch.softmax(outputs, dim=1)

        confidence, prediction = torch.max(probabilities, 1)

    predicted_class = label_map[str(prediction.item())]

    return predicted_class, confidence.item()
