from flask import Flask, escape, request, Response
from translate_photo import translate_photo

app = Flask(__name__)

@app.route('/')
def main():
    #face decode automat din url encoding
    encoded_image = request.args.get("image")
    language = request.args.get("language")
    if language is None:
        language = 'en'
    return translate_photo(encoded_image, language)
    #return Response(translate_photo(encoded_image, language), mimetype='image/jpeg')


