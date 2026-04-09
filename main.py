from src.preprocessing import limpiar_texto
from src.keybert_extractor import extraer_keybert
from src.rake_extractor import extraer_rake
from src.tf_idf_extractor  import extraer_tfidf

def main():
    with open("data/raw/texto.txt", "r", encoding="utf-8") as f:
        texto = f.read()

    texto_limpio = limpiar_texto(texto)

    print("\n--- KEYBERT ---")
    print(extraer_keybert(texto_limpio))

    print("\n--- RAKE ---")
    print(extraer_rake(texto_limpio))

    print("\n--- TF-IDF ---")
    print(extraer_tfidf(texto_limpio))


if __name__ == "__main__":
    main()