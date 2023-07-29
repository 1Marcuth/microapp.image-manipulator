from fastapi import APIRouter, UploadFile, File, Response
from fastapi.responses import JSONResponse
from typing import Literal
import os

from utils.image import convert_image, crop_image, resize_image, rotate_image
from utils.random import generate_random_filename
from utils.api_request import save_request_file

AcceptableImageFormats = Literal["jpeg", "jpg", "png", "webp", "dds", "gif"]

image_manipulator_router = APIRouter()

current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
root_dir = os.path.join(current_dir, "..", "..", "..")
tmp_dir = os.path.join(root_dir, ".tmp")

@image_manipulator_router.post("/convert")
def convert_image_handler(
    input: AcceptableImageFormats,
    output: AcceptableImageFormats,
    file: UploadFile = File(...)
):
    if (input == "jpg" and output == "jpeg") or input == output:
        return JSONResponse(
            content = { "message": "Input and output file formats cannot be the same." },
            status_code = 400
        )
    
    input_filename = generate_random_filename(input)
    output_filename = input_filename.replace(f".{input}", f".{output}")
    input_file_path = os.path.join(tmp_dir, input_filename)
    output_file_path = os.path.join(tmp_dir, output_filename)

    save_request_file(input_file_path, file)

    file_content = convert_image(
        input_file_path = input_file_path, 
        output_file_path = output_file_path,
        output_format = output
    )

    return Response(
        content = file_content,
        status_code = 201,
        media_type = f"image/{output}"
    )

@image_manipulator_router.post("/resize")
def resize_image_handler(
    input: AcceptableImageFormats,
    width: int,
    height: int,
    file: UploadFile = File(...)
):
    input_filename = generate_random_filename(input)
    input_file_path = os.path.join(tmp_dir, input_filename)

    save_request_file(input_file_path, file)

    output_filename = input_filename.replace(f".{input}", f"_{width}x{height}.{input}")
    output_file_path = os.path.join(tmp_dir, output_filename)

    file_content = resize_image(
        input_file_path = input_file_path,
        output_file_path = output_file_path,
        width = width,
        height = height
    )

    return Response(
        content = file_content,
        status_code = 201,
        media_type = f"image/{input}"
    )

@image_manipulator_router.post("/crop")
def crop_image_handler(
    input: AcceptableImageFormats,
    top: int,
    left: int,
    width: int,
    height: int,
    file: UploadFile = File(...),
):
    input_filename = generate_random_filename(input)
    input_file_path = os.path.join(tmp_dir, input_filename)

    save_request_file(input_file_path, file)

    output_filename = input_filename.replace(f".{input}", f"_crop.{input}")
    output_file_path = os.path.join(tmp_dir, output_filename)

    file_content = crop_image(
        input_file_path = input_file_path,
        output_file_path = output_file_path,
        top = top,
        left = left,
        width = width,
        height = height,
    )

    return Response(
        content=file_content,
        status_code=201,
        media_type=f"image/{input}",
    )


@image_manipulator_router.post("/rotate")
def rotate_image_handler(
    input: AcceptableImageFormats,
    angle: int,
    file: UploadFile = File(...),
):
    input_filename = generate_random_filename(input)
    input_file_path = os.path.join(tmp_dir, input_filename)

    save_request_file(input_file_path, file)

    output_filename = input_filename.replace(f".{input}", f"_rotate.{input}")
    output_file_path = os.path.join(tmp_dir, output_filename)

    file_content = rotate_image(
        input_file_path = input_file_path,
        output_file_path = output_file_path,
        angle = angle,
    )

    return Response(
        content=file_content,
        status_code=201,
        media_type=f"image/{input}",
    )