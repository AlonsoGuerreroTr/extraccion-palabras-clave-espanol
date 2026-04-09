# Extracción de palabras clave en español 

Proyecto enfocado en la **extracción de palabras clave en español** con el uso de KeyBert, RAKE, TF-Idf


---

## Objetivo

Preparar datos textuales en español eliminando ruido común como:

* Caracteres corruptos (ej: `cÃ³mo`)
* Stopwords
* Variaciones de acentos

---
## Instalación

Clona el repositorio:

```bash
gh repo clone AlonsoGuerreroTr/evaluador_nivel_espanol
cd extraccion-palabras-clave-español
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```


## Estructura del proyecto

```text
extraccion-palabras-clave-español/
│
├── data/
│   ├── raw/              # Datos originales
│   └── 
│
├── notebooks/            # Exploración y pruebas
│
├── src/
│   ├── preprocessing.py       # Preparar el texto
│   └── keybert_extractor.py  # Extraccion con KeyBERT
│   └── rake_extractor.py  # Extraccion con RAKE
│   └── tf_idf_extractor.py  # Extraccion con TF-Idf
│
├── main.py               # Script principal
├── requirements.txt
└── README.md
```

---


## Uso

Ejecuta el script principal:

```bash
python main.py
```

Esto:

1. Carga el texto desde `data/raw/`
2. Aplica el preprocesamiento
3. Procesa el texto con los diferentes métodos


---

##  Ejemplo de lematización

### Entrada:

```
El profesor, como tal, no va a asumir las tres funciones a la vez, sino que lo hará de acuerdo con la propia dinámica del grupo y de las actividades de la clase. Siendo un analista de las necesidades a la hora de establecer el currículo del grupo o cuando encuentre nuevos requerimientos en los alumnos que no había descubierto anteriormente, incluso podrá ser consejero y gestor de la clase de forma complementaria en las actividades comunicativas, y además puede dejar de lado una actuación como profesor comunicativo, aquel que fomenta y enseña dicha competencia lingüista en los estudiantes. Dentro de mi propuesta los papeles que va a representar el profesor serán el consejero y el gestor de los procesos de grupo: por un lado va a ayudar al estudiante sobre todo en la lectura del texto literario en caso de que tenga alguna duda o problema;  por el otro lado, va a ayudar a los aprendientes con la realización de las actividades que harán en clase, ya que los ejercicios  y, sobre todo, la lectura del texto podrían representar un reto muy difícil para los alumnos de nivel básico que no estén acostumbrados a este tipo de ejercicios.
```

### Salida:

```
KEYBERT ---
 [('clase', 0.5153), ('profesor', 0.4717), ('curriculo', 0.4619), ('aprendientes', 0.4562), ('estudiante', 0.4258)]

RAKE ---
('descubierto anteriormente', 4.0), ('forma complementaria', 4.0), ('nivel basico', 4.0), ('esten acostumbrados', 4.0)

TF-IDF ---
('actividades', (0.2822162605150792)), ('clase', (0.2822162605150792)), ('grupo', (0.2822162605150792))
```

---

## Tecnologías usadas

* Python
* spaCy
* RAKE
* KeyBert
* TF-Idf


---

## Autor

Proyecto desarrollado por [Alonso Guerrero]

---

## Licencia

Este proyecto es de uso educativo y libre.
