from fastapi import UploadFile
import shutil

def save_request_file(file_path: str, file: UploadFile) -> None:
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)