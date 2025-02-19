# **AUGMENTED DOCUMENT READER**

## **📌 The Application**
The **AUGMENTED DOCUMENT READER** application features a **Streamlit-based graphical interface**, allowing users to perform **Named Entity Recognition (NER)** on uploaded documents.

Two file formats are supported: **TXT and DOCX**. The user **uploads a file**, and the appropriate **NER algorithm is automatically triggered**. The result is provided in **JSON format**.

The different types of NER implemented are **tested directly in the notebook** `named_entity_recognation.ipynb`:
- **Rule-Based NER** (using predefined rules)
- **Open Source Model-Based NER** (using pre-trained models)
- **LLM/RAG-Based NER** (leveraging a language model and a retrieval-augmented system)

For **LLM/RAG-Based NER**, I implemented a **RAG system** using **Langchain, FAISS, and Mistral (via Ollama)** locally.

## **🔹 The NER App:**
![The NER App](src/images/app.png)

## **🔹 Rule-Based Entity Extraction (DOCX File):**
![The NER App](src/images/v_docx.png)

## **🔹 NLP Model-Based Entity Extraction (TXT File):**
![The NER App](src/images/v_txt.png)

---

## **💡 How to Build a NER Model for Financial Data?**
You can **fine-tune** a pre-trained NER model on your own financial data.

### **1️⃣ Data Collection**
- Gather **annotated financial documents**.  
- Label financial entities (**ORG, MONEY, INSTRUMENT, DATE, etc.**) using the **BIO format** for example.  
- Clean and preprocess the data for compatibility.  

### **2️⃣ Fine-Tuning**
- Choose a **pre-trained NER model** (e.g., Hugging Face).  
- Train only the **classification head** while **freezing** the early layers of the model.  

## **🚀 How to Run the APP**
#### Install Dependencies**
Before running the app, install all required dependencies using:
```bash
pip install -r requirements.txt
```

#### Launch the ST App**
Move to the root directory of the project and Run:
```bash
streamlit run app.py
```
---

🚀 **The goal: an optimized model to accurately extract financial entities!**
