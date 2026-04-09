from keybert import KeyBERT

model = KeyBERT("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

def extraer_keybert(texto):
    keywords = model.extract_keywords(texto)
    keywords_ngram = model.extract_keywords(texto, keyphrase_ngram_range=(1,2))
    
    return {
        "keywords": keywords,
        "keywords_ngram": keywords_ngram
    }

