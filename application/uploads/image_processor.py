import os
import hashlib
from PIL import Image
from flask import current_app


def hash_filename(filename, hash_length=32):
    """
    Hash a filename and return the hash
    :param filename:
    :param hash_length:
    :return string
    """
    salt = os.urandom(16)
    salted_name = salt + str.encode(filename)
    hashed_name = hashlib.sha256(salted_name).hexdigest()

    truncated_hash_name = hashed_name[:hash_length]

    return truncated_hash_name


def process_image(image_upload, user_id):
    """
    :param image_upload:
    :param user_id:
    :return: tuple of (filename, filepath)
    """

    filename = image_upload.filename
    new_filename = str(user_id) + "_" + hash_filename(filename) + filename
    filepath = os.path.join(current_app.root_path, "static", new_filename)
    current_app.logger.info(f"Saving image to {filepath}")
    with Image.open(image_upload) as img:
        # Resize the image
        # resized_img = img.resize((224, 224), Image.Resampling.LANCZOS)

        # resized_
        img.save(filepath)

    return new_filename, filepath
