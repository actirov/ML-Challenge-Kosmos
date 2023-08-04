import spacy

def recognize_entities(sentences):
    nlp = spacy.load("es_core_news_sm") # Cargar el modelo de idioma español
    entities = [] # Esta lista almacenará las entidades reconocidas en cada frase.
    
    for sentence in sentences:
        doc = nlp(sentence) # Procesar la oración con el modelo de lenguaje.
        entities_in_sentence = {ent.text: ent.label_ for ent in doc.ents} # Almacenar las entidades en un diccionario.
        entities.append({"oración": sentence, "entidades": entities_in_sentence}) # Agregar el diccionario a la lista de entidades.
    
    return entities # Devuelve la lista de entidades.

