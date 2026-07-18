import os
from PIL import Image
from torch.utils.data import Dataset

class LungDataset(Dataset):

    def __init__(self, root_dir, transform=None):

        self.root_dir = root_dir
        self.transform = transform

        # Get class names (BACTERIA, VIRUS)
        self.classes = sorted([
            folder
            for folder in os.listdir(root_dir)
            if os.path.isdir(os.path.join(root_dir, folder))
        ])

        # Create label mapping
        self.class_to_idx = {
            class_name: idx
            for idx, class_name in enumerate(self.classes)
        }

        self.samples = []

        # Read every image
        for class_name in self.classes:

            class_folder = os.path.join(root_dir, class_name)

            for image_name in os.listdir(class_folder):

                image_path = os.path.join(class_folder, image_name)

                self.samples.append(
                    (image_path, self.class_to_idx[class_name])
                )

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):

        image_path, label = self.samples[index]

        image = Image.open(image_path).convert("RGB")

        if self.transform:
            image = self.transform(image)

        return image, label
