from fastapi import APIRouter, HTTPException, UploadFile, File
from Schemas.translation_schema import TranslationCreateSchema, TranslationSchema
from Service.service_translation import create_translation, get_translation_by_id, get_all_translations, update_translation, delete_translation

router = APIRouter()

@router.post("/translations", response_model=TranslationSchema)
async def create_translation_endpoint(name: str, file: UploadFile = File(...)):
    try:
        file_path = f"uploads/{file.filename}"
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())
        data = TranslationCreateSchema(name=name, pdf=file_path)
        return await create_translation(data)

    except Exception as error:
        return f"Erro em create_translation_endpoint: {str(error)}"


@router.get("/translations/{translation_id}", response_model=TranslationSchema)
async def get_translation_endpoint(translation_id: str):
    try:
        translation = await get_translation_by_id(translation_id)
        if not translation:
            raise HTTPException(status_code=404, detail="Translation not found")
        return translation

    except Exception as error:
        return f"Erro em get_translation_endpoint: {str(error)}"


@router.get("/translations", response_model=list[TranslationSchema])
async def get_all_translations_endpoint():
    try:
        return await get_all_translations()

    except Exception as error:
        return f"Erro em get_all_translations_endpoint: {str(error)}"


@router.put("/translations/{translation_id}", response_model=TranslationSchema)
async def update_translation_endpoint(translation_id: str, name: str, file: UploadFile = File(...)):
    try:
        file_path = f"uploads/{file.filename}"
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())
        data = TranslationCreateSchema(name=name, pdf=file_path)
        updated_translation = await update_translation(translation_id, data)
        if not updated_translation:
            raise HTTPException(status_code=404, detail="Translation not found")
        return updated_translation

    except Exception as error:
        return f"Erro em update_translation_endpoint: {str(error)}"


@router.delete("/translations/{translation_id}")
async def delete_translation_endpoint(translation_id: str):
    try:
        success = await delete_translation(translation_id)
        if not success:
            raise HTTPException(status_code=404, detail="Translation not found")
        return {"message": "Translation deleted successfully"}

    except Exception as error:
        return f"Erro em delete_translation_endpoint: {str(error)}"