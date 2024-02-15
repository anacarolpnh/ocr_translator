from fastapi import APIRouter
from Service.build_json import created_data_extract_register
from Model.dto.insert_register_dto import InserRegisterDTO

class InsertRegister:
    router = APIRouter()

    @router.post('/insert_register')
    async def router_saved_files(register: InserRegisterDTO):
            result = await created_data_extract_register(register)
            return result

    @classmethod
    def to_router(cls):
        return cls.router


class SearchRegisterByName:
    router = APIRouter()

    @router.get('/get_register_by_name')
    async def router_get_register_by_name(name_register):
        result = await get_register(name_result)
        return result

    @classmethod
    def to_router(cls):
        return cls.router


class GetRegisters:
    router = APIRouter()

    @router.get('/get_registers')
    async def get_config():
        result = await router_get_registers()
        return result

    @classmethod
    def to_router(cls):
        return cls.router