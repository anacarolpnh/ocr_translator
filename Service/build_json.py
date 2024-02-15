from Service.process_file import extract_text

async def created_data_extract_register(register):
    try:
        await extract_text(register.file)
        name:str = register.name
        file:bytes = register.file
        original_text = "texto original extraido"
        translate_text = "texto traduzido"
        
    except Exception as error:
       return error
