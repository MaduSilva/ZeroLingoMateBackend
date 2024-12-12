from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

def translate_ptbr_to_eng_to_kr(text):
    try:
        engTranslation = GoogleTranslator(source='pt', target='en').translate(text)

        krTranslation = GoogleTranslator(source='en', target='ko').translate(engTranslation)
        
        return engTranslation, krTranslation
    except Exception as e:
        print(f"error during translation: {e}")
        return None, None

@app.route('/translate', methods=['POST'])
def translate():

    data = request.get_json()

    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "missing text"}), 400
    
    engTranslation, krTranslation = translate_ptbr_to_eng_to_kr(text)

    if engTranslation and krTranslation:
        return jsonify({
            "original": text,
            "english_translation": engTranslation,
            "korean_translation": krTranslation
        }), 200

    else:
        return jsonify({"error": "internal service error"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8081, host='0.0.0.0')
