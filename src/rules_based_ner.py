from langchain_community.document_loaders import Docx2txtLoader
from transformers import pipeline
import re
import json

#Lire un fichier docx et extraire son texte.
def extract_text_from_docx(docx_path):
    data  = Docx2txtLoader(docx_path).load()
    return data[0].page_content.strip()

#Génèrer les regex à des noms d'entités qu'on souhaite extraire
def format_entity_patterns(entity_names):
    return [rf"{re.escape(name)}\s*\n(.+)" for name in entity_names]


#Appliquer les regex pour extraire des entités nommées
def extract_entities_rules_based(text,
                      entities_names =  ["Counterparty", "Initial Valuation Date", "Notional", "Valuation Date", "Maturity", "Underlying", "Coupon", "Barrier", "Calendar"], 
                      entities_to_extract = ["Party A", "Initial Valuation Date", "Notional Amount (N)", "Valuation Date", "Termination Date",  "Underlying", "Coupon (C)", "Barrier (B)", "Business Day"]):
    entities = {}
    patterns = dict(zip(entities_names,  format_entity_patterns(entities_to_extract)))
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        entities[key] = match.group(1) if match else None
    return entities