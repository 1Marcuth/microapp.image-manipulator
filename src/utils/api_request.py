from fastapi import UploadFile
import shutil
import os

def save_request_file(file_path: str, file: UploadFile) -> None:
    os.makedirs(
        name = os.path.dirname(file_path),
        exist_ok = True
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)