
import cv2
import pytesseract
import re


async def extract_text(register):
    try:
        image_path = register
        imagem = cv2.imread(image_path)
        # Converter a região de interesse para escala de cinza
        gray_roi = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray_roi)
        
    except Exception as error:
       return error
