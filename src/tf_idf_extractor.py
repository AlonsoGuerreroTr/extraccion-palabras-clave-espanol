from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from spacy.lang.es import STOP_WORDS

# convertir stopwords a lista
spanish_stopwords = list(STOP_WORDS)


def extraer_tfidf(texto, top_n=5):
    # vectorización
    vectorizer = CountVectorizer(
        stop_words=spanish_stopwords,
        max_df=1.0,
        min_df=1
    )

    word_counts = vectorizer.fit_transform([texto])
    features = vectorizer.get_feature_names_out()

    # TF-IDF
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(word_counts)

    # convertir a formato ordenable
    coo = tfidf_matrix.tocoo()
    tuples = zip(coo.row, coo.col, coo.data)

    # ordenar por importancia
    sorted_items = sorted(tuples, key=lambda x: x[2], reverse=True)

    # top palabras clave
    top_keywords = [
        (features[col], score)
        for _, col, score in sorted_items[:top_n]
    ]

    return top_keywords