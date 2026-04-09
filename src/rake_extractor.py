from multi_rake import Rake
from spacy.lang.es import STOP_WORDS

rake = Rake(
    language_code="es",
    stopwords=STOP_WORDS
)

def extraer_rake(texto):
    resultados = rake.apply(texto)
    return resultados[:10]