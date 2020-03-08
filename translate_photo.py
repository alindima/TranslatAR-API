import io
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from googletrans import Translator

def translate_photo(image_bytes, language='en'):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    image = Image.open(io.BytesIO(image_bytes))

    source_text = pytesseract.image_to_string(image)

    translator = Translator()
    result = translator.translate(source_text, dest=language)
    return result.text
