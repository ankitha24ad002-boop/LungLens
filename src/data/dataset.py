import os
from PIL import Image
from torch.utils.data import Dataset

class LungDataset(Dataset):

    def __init__(self, root_dir, transform=None):

        self.transform = transform
        self.samples = []

        self.class_names = sorted(
            [
                folder
                for folder in os.listdir(root_dir)
                if os.path.isdir(os.path.join(root_dir, folder))
            ]
        )

        self.class_to_idx = {
            cls: idx
            for idx, cls in enumerate(self.class_names)
        }

        for cls in self.class_names:

            class_folder = os.path.join(root_dir, cls)

            for image_name in os.listdir(class_folder):

                image_path = os.path.join(class_folder, image_name)

                self.samples.append(
                    (
                        image_path,
                        self.class_to_idx[cls]
                    )
                )

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):

        image_path, label = self.samples[index]

        image = Image.open(image_path).convert("RGB")

        if self.transform:
            image = self.transform(image)

        return image, label
