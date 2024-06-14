from pydantic import BaseModel
from datetime import datetime

class TranslationSchema(BaseModel):
    name: str
    pdf: str
    timestamp: datetime
    translated_text: str

class TranslationCreateSchema(BaseModel):
    name: str
    pdf: str
