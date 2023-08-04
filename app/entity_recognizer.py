import spacy

def recognize_entities(sentences):
    nlp = spacy.load("es_core_news_sm")
    entities = []
    
    for sentence in sentences:
        doc = nlp(sentence)
        entities_in_sentence = {ent.text: ent.label_ for ent in doc.ents}
        entities.append({"oración": sentence, "entidades": entities_in_sentence})
    
    return entities

