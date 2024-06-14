from pydantic import BaseModel
from datetime import datetime

class Translation(BaseModel):
    id: str
    name: str
    pdf: str
    timestamp: datetime
    translated_text: str
