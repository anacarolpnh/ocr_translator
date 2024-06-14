import os
import datetime
from googletrans import Translator
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from Models.register_model import Translation
from Schemas.translation_schema import TranslationCreateSchema, TranslationSchema
from Utils.utils_pdf import extract_text_from_pdf
from db.database import MONGO_URI, DATABASE_NAME

translator = Translator()

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db['translations']

async def create_translation(data: TranslationCreateSchema) -> TranslationSchema:
    try:
        pdf_path = data.pdf
        extracted_text = extract_text_from_pdf(pdf_path)
        translated = translator.translate(extracted_text, dest='pt').text
        
        translation = Translation(
            id=str(ObjectId()),
            name=data.name,
            pdf=pdf_path,
            timestamp=datetime.datetime.now(),
            translated_text=translated
        )
        
        await collection.insert_one(translation.dict())
        await clear_uploads_directory()
        return TranslationSchema(**translation.dict())
    
    except Exception as error:
        return f"Erro ao criar tradução: {str(error)}"


async def get_translation_by_id(translation_id: str) -> TranslationSchema:
    try:
        translation = await collection.find_one({"id": translation_id})
        if translation:
            return TranslationSchema(**translation)
        return None
    
    except Exception as error:
        return f"Erro ao buscar tradução por ID: {str(error)}"


async def get_all_translations() -> list[TranslationSchema]:
    try:
        translations = await collection.find().to_list(100)
        return [TranslationSchema(**translation) for translation in translations]
    
    except Exception as error:
        return f"Erro ao buscar todas as traduções: {str(error)}"


async def update_translation(translation_id: str, data: TranslationCreateSchema) -> TranslationSchema:
    try:
        pdf_path = data.pdf
        extracted_text = extract_text_from_pdf(pdf_path)
        translated = translator.translate(extracted_text, dest='pt').text
        
        updated_translation = await collection.find_one_and_update(
            {"id": translation_id},
            {"$set": {"name": data.name, "pdf": pdf_path, "translated_text": translated, "timestamp": datetime.datetime.now()}},
            return_document=True
        )
        
        await clear_uploads_directory()
        
        if updated_translation:
            return TranslationSchema(**updated_translation)
        return None
    
    except Exception as error:
        return f"Erro ao atualizar tradução: {str(error)}"


async def delete_translation(translation_id: str):
    try:
        result = await collection.delete_one({"id": translation_id})
        return result.deleted_count > 0
    
    except Exception as error:
        return f"Erro ao deletar tradução: {str(error)}"


async def clear_uploads_directory():
    uploads_dir = 'uploads'
    
    try:
        for filename in os.listdir(uploads_dir):
            file_path = os.path.join(uploads_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

    except Exception as error:
        return f"Erro ao limpar o diretório uploads: {str(error)}"
