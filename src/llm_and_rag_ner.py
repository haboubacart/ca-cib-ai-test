from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import ollama
import json
import re


def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=0)
    chunks = []
    for page in docs:
        text = page.page_content.strip()
        if text:
            chunks.extend(text_splitter.split_text(re.sub(r'\s+', ' ', text).strip() ))
    return chunks



def index_documents(list_chunks, embedding_model, index_path) : 
    print("starting indexation in FAISS")
    store = FAISS.from_texts(list_chunks, embedding_model)
    store.save_local(index_path)
    print("indexation terminated")



def retrieve_relevant_data(retriever, query) :
    results = retriever.similarity_search(query, k=4)
    source_knowledge = "\n".join([x.page_content for x in results])
    return source_knowledge


def extract_named_entities(text, model='mistral') :   
    print('NER performing')
    prompt = f"""
    Identify the **financial named entities** in the following text.
    Extract only relevant financial entities and return a valid JSON object with:
    - "ORG": Financial organizations (banks, investment firms)
    - "MONEY": Monetary amounts and currencies
    - "DATE": Financial dates (maturity, contract dates)
    - "PERCENT": Percentages (interest rates, stock growth)
    - "INSTRUMENT": Financial instruments (stocks, bonds, derivatives)
    ---
    {text}
    ---
    Return only a JSON object in this format for example:
    {{
      "ORG": ["BankABC", "Infuse Capital", "Surya Power Magic Private Limited"],
      "MONEY": ["$10 million", "INR 10,000", "Rs. 400,000"],
      "DATE": ["Q1 2023", "January 2025", "60 months Exit Period"],
      "INSTRUMENT": ["Convertible Preference Shares", "Tesla bonds", "Stock options"],
      "PERCENT": ["25% IRR", "1% dividend rate", "3.5% interest rate"],
      "SHAREHOLDER": ["Existing Shareholders XX", "Sponsor", "Key Persons"],
      "EXIT_STRATEGY": ["Qualified IPO", "Share Buyback", "Acquisition"],
      "LEGAL_TERM": ["Drag Along Rights", "Tag Along Rights", "Voting Rights", "Anti-dilution"]
    }}
    If no financial entities are found, return an empty JSON with these keys
    Do not include explanations, comments, or any extra text.
    """
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    print('NER finished')
    return json.loads(response["message"]["content"])
    