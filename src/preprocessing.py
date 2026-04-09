import re
from unidecode import unidecode

def limpiar_texto(texto):
    texto = texto.lower()
    texto = unidecode(texto)
    texto = re.sub(r'[^a-zñáéíóúü\s]', '', texto)
    return texto