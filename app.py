from flask import Flask, request
from translate_photo import translate_photo

app = Flask(__name__)

# Imaginea trebuie trimisa ca raw bytes
@app.route('/', methods=['POST'])
def main():
    #Trebuie facuta o verificare, daca nu e nimic in request o sa dea 500
    image_bytes = request.stream.read()
    language = request.args.get("language")
    if language is None:
        language = 'en'
    return translate_photo(image_bytes, language)

