import spacy
from spacy.matcher import Matcher
from datetime import datetime

# Cargar el modelo de spaCy en español
nlp = spacy.load("es_core_news_sm")

# Crear un matcher para buscar patrones
matcher = Matcher(nlp.vocab)

# Añadir patrones para identificar fechas
date_patterns = [
    [{"SHAPE": "dd/dd/dddd"}],  # Fechas como 24/12/2024
    [{"LOWER": {"REGEX": r"\d{1,2} de [a-z]+"}}],  # Fechas como "24 de diciembre"
]
matcher.add("DATE", date_patterns)

# Añadir patrones para ubicaciones comunes
location_patterns = [
    [{"ENT_TYPE": "LOC"}],  # Nombres de lugares reconocidos por spaCy
]
matcher.add("LOCATION", location_patterns)

# Procesar un texto de ejemplo
text = """
Te invitamos al evento 'Conferencia sobre Inteligencia Artificial' el 24 de diciembre de 2024 
en el Centro de Convenciones de Bogotá. Discutiremos avances y nuevos proyectos relacionados 
con el uso ético de la inteligencia artificial.
"""
doc = nlp(text)

# Aplicar el matcher
matches = matcher(doc)

# Extraer información clave
event_info = {
    "date": [],
    "location": [],
    "topics": [],
}

for match_id, start, end in matches:
    span = doc[start:end]
    label = nlp.vocab.strings[match_id]
    if label == "DATE":
        event_info["date"].append(span.text)
    elif label == "LOCATION":
        event_info["location"].append(span.text)

# Extraer temas principales usando entidades nombradas
topics = [ent.text for ent in doc.ents if ent.label_ == "MISC"]
event_info["topics"].extend(topics)

# Imprimir resultados
print("Información extraída:")
print(f"Fechas: {', '.join(event_info['date'])}")
print(f"Ubicaciones: {', '.join(event_info['location'])}")
print(f"Temas: {', '.join(event_info['topics'])}")
