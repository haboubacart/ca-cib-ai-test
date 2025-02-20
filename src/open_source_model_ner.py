from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

#Lire une fichier txt et extraire le contenu
def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

#Lire un ficher uploadé sur l'interface streamlit et  extraire son contenu
def st_read_text_file(uploaded_file):
    return uploaded_file.getvalue().decode("utf-8")

#Charger le  modele de NER et initialiser le pipeline
def model_loader(model_path) :
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForTokenClassification.from_pretrained(model_path)
    return pipeline("ner", model=model, tokenizer=tokenizer,  aggregation_strategy="first")

#Realiser l'extration des entites avec le modèle de NER
def extract_named_entities_open_source_model(ner_pipeline, text) :
    results = ner_pipeline(text)
    entities = [{k: d[k] for k in ["entity_group", "score", "word"]} for d in results]
    return entities