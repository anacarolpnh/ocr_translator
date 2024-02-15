from pydantic import BaseModel


class RegisterDTO(BaseModel):
    name: str
    file: bytes
    original_text: str
    translate_text: str