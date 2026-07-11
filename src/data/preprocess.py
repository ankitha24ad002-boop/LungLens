import os
import cv2
import numpy as np


def preprocess_image(input_path, output_path, size=(224, 224)):

    image = cv2.imread(input_path)

    if image is None:
        print("Cannot read:", input_path)
        return

    # Resize image
    image = cv2.resize(image, size)

    # Normalize pixels
    image = image / 255.0

    # Convert back to image format
    image = (image * 255).astype(np.uint8)

    # Save image
    cv2.imwrite(output_path, image)


def preprocess_folder(input_folder, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):

        if file.endswith(".jpeg") or file.endswith(".jpg"):

            input_path = os.path.join(
                input_folder,
                file
            )

            output_path = os.path.join(
                output_folder,
                file
            )

            preprocess_image(
                input_path,
                output_path
            )

            print("Processed:", file)


if __name__ == "__main__":

    preprocess_folder(
        "data/raw",
        "data/processed"
    )
