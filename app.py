import streamlit as st
import os
from src.open_source_model_ner import (model_loader,
                                       st_read_text_file,
                                       extract_named_entities_open_source_model)


from src.rules_based_ner import  (extract_entities_rules_based,
                                  st_extract_text_from_docx,
                                  extract_text_from_docx)

embedding_model_path = "pretrained-models/all-MiniLM-L6-v2"
ner_model_path = "./pretrained-models/distilbert-NER"
ner_pipeline = model_loader(ner_model_path)



# Streamlit App
st.set_page_config(page_title="NER App", page_icon="📄")
st.image("./data/logo2.png", width=500)
st.title("CMI · ADOR - NER APP")
st.write("Upload a TXT or DOCX file to extract named entities.")

# File uploader
uploaded_file = st.file_uploader("Upload a file", type=["txt", "docx"])

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1]
    
    if file_type == "txt":
        text = st_read_text_file(uploaded_file)
        st.write("### Extracted Text:")
        st.text_area("Text Content", text, height=100)
        
        # Apply rule-based entity extraction
        st.write("### Extracted Named Entities:")
        entities = extract_named_entities_open_source_model(ner_pipeline, text)
        st.json(entities)
        
    elif file_type == "docx":
        text = st_extract_text_from_docx(uploaded_file)
        st.write("### Extracted Text:")
        st.text_area("Text Content", text, height=100)
        
        # Apply open-source model-based entity extraction
        st.write("### Extracted Named Entities:")
        entities = extract_entities_rules_based(text)
        st.json(entities)
    
    else:
        st.error("Unsupported file format. Please upload a TXT or DOCX file.")
