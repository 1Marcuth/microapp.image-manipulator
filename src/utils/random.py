from pydantic import validate_call
import uuid

@validate_call
def generate_random_filename(extension: str) -> str:
    filename = str(uuid.uuid1()) + f".{extension}"
    return filename