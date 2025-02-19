from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline


def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
def model_loader(model_path) :
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForTokenClassification.from_pretrained(model_path)
    return pipeline("ner", model=model, tokenizer=tokenizer,  aggregation_strategy="first")


def extract_named_entities_open_source_model(ner_pipeline, text) :
    results = ner_pipeline(text)
    entities = [{k: d[k] for k in ["entity_group", "score", "word"]} for d in results]
    return entities