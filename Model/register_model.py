from typing import List
from Model.dto.register_dto import RegisterDTO

async def register_serial(RegisterDTO) -> dict:
    try:
        return {
            "id": str(RegisterDTO["_id"]),
            "name": RegisterDTO["name"],
            "file": RegisterDTO["file"],
            "original_text": RegisterDTO["original_text"],
            "translate_text": RegisterDTO["translate_text"],
        }
        
    except Exception as error:
        print(f"Erro na função register_serial: {str(error)}")


async def register_list(RegisterList: List[RegisterDTO]) -> List[dict]:
    try:
        return [await register_serial(Register) for Register in RegisterList]

    except Exception as error:
        print(f"Erro na função register_list: {str(error)}")
