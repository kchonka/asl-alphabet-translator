# Utility methods

import os
import base64

from constants import DATASET_FILE_ROOT, PNG_EXTENSION, DATASET_FOLDER
from constants import ERROR_UNABLE_TO_DECODE


def get_image_path(letter: str):
    """Return the correct image path based on the letter."""
    file_name = f"{DATASET_FILE_ROOT}{letter}{PNG_EXTENSION}"
    file_path = os.path.abspath(os.path.join(DATASET_FOLDER, file_name))
    print(f"Retrieving image {file_path}")
    return file_path


def get_encoded_image(file_path: str):
    """Given a file_path to a letter image, encode the image in base-64."""

    try:
        with open(file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            return encoded_string
    except Exception as err:
        print(ERROR_UNABLE_TO_DECODE)
        return None
