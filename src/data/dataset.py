import os
from torch.utils.data import Dataset
from PIL import Image


class LungDataset(Dataset):

    def __init__(self, image_dir, transform=None):

        self.image_dir = image_dir
        self.transform = transform

        self.images = os.listdir(image_dir)


    def __len__(self):

        return len(self.images)


    def __getitem__(self, index):

        image_name = self.images[index]

        image_path = os.path.join(
            self.image_dir,
            image_name
        )

        image = Image.open(image_path).convert("RGB")


        # Assign labels
        if "BACTERIA" in image_name:
            label = 0

        elif "VIRUS" in image_name:
            label = 1

        else:
            label = -1


        if self.transform:
            image = self.transform(image)


        return image, label
