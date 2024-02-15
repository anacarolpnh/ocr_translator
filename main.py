from fastapi import FastAPI
from Controller.registers_controllers import *

app = FastAPI()

insert_register = InsertRegister()
get_register = GetRegisters()
search_register_by_name = SearchRegisterByName()


app.include_router(insert_register.to_router())
app.include_router(get_register.to_router())
app.include_router(get_register.to_router())



