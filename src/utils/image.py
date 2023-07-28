from pydantic import validate_call
from PIL import Image
import os

images_without_transparency = [ "jpeg", "jpg" ]

@validate_call
def convert_image(
    input_file_path: str,
    output_file_path: str,
    output_format: str
) -> bytes:
    img = Image.open(input_file_path)

    if output_format in images_without_transparency and img.mode == "RGBA":
        img = img.convert("RGB")

    img.save(
        fp = output_file_path,
        format = "jpeg" if output_format == "jpg" else output_format,
        quality = 100
    )

    with open(output_file_path, "rb") as file:
        file_content = file.read()

    os.remove(input_file_path)
    os.remove(output_file_path)

    return file_content

def resize_image(
    input_file_path: str,
    output_file_path: str,
    width: int,
    height: int,
) -> bytes:
    img = Image.open(input_file_path)
    img = img.resize((width, height))

    img.save(output_file_path)

    with open(output_file_path, "rb") as file:
        file_content = file.read()

    os.remove(input_file_path)
    os.remove(output_file_path)

    return file_content

@validate_call
def crop_image(
    input_file_path: str,
    output_file_path: str,
    left: int,
    top: int,
    width: int,
    height: int,
) -> bytes:
    img = Image.open(input_file_path)
    right = left + width
    bottom = top + height
    img = img.crop((left, top, right, bottom))

    img.save(output_file_path)

    with open(output_file_path, "rb") as file:
        file_content = file.read()

    os.remove(input_file_path)
    os.remove(output_file_path)

    return file_content

@validate_call
def rotate_image(
    input_file_path: str,
    output_file_path: str,
    angle: int
) -> bytes:
    img = Image.open(input_file_path)

    rotated_img = img.rotate(
        angle = angle,
        resample = Image.BICUBIC,
        expand = True
    )

    rotated_img.save(output_file_path)

    with open(output_file_path, "rb") as f:
        file_content = f.read()

    os.remove(input_file_path)
    os.remove(output_file_path)

    return file_content