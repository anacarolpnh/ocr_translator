from pydantic import BaseModel


class InserRegisterDTO(BaseModel):
    name: str
    file: bytes
