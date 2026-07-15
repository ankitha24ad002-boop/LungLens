# src/models/predict.py (Dummy version for Person 4 to use immediately)
import json
from PIL import Image

import torch
import torch.nn as nn

from torchvision import transforms, models

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = models.resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features,2)

model.load_state_dict(torch.load("models/best_model.pth",map_location=device))
model.to(device)
model.eval()

with open("models/label_map.json","r") as f:
    label_map = json.load(f)

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

def predict_image(image_path):

    image = Image.open(image_path).convert("RGB")

    image = transform(image)

    image = image.unsqueeze(0)

    image = image.to(device)

    with torch.no_grad():

        output = model(image)

        prediction = torch.argmax(output,1).item()

    return label_map[str(prediction)]
