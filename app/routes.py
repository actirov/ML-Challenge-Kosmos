from flask import request, jsonify
from app import app
from app.entity_recognizer import recognize_entities

@app.route('/ner', methods=['POST'])
def named_entity_recognition():
    data = request.get_json()
    sentences = data.get("oraciones", [])

    if not sentences or not isinstance(sentences, list):
        return jsonify({"error": "The 'oraciones' field must be a list of sentences."}), 400
    
    entities = recognize_entities(sentences)

    return jsonify({"resultado": entities}), 200
