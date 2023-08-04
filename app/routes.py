from flask import request, jsonify
from app import app
from app.entity_recognizer import recognize_entities

@app.route('/ner', methods=['POST']) # Esta ruta acepta solicitudes POST en la URL /ner.
def named_entity_recognition():
    data = request.get_json() # Obtener los datos JSON enviados con la solicitud.
    sentences = data.get("oraciones", []) # Extrae las oraciones de los datos.

    # Compruebe si las oraciones se proporcionan correctamente.
    if not sentences or not isinstance(sentences, list):
        return jsonify({"error": "The 'oraciones' field must be a list of sentences."}), 400 # Devuelve un error si las oraciones no se proporcionan correctamente.
    
    entities = recognize_entities(sentences) # Obtener las entidades reconocidas para cada oración.

    return jsonify({"resultado": entities}), 200 # Devuelve una respuesta JSON con las entidades.

