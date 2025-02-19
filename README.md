# **AUGMENTED DOCUMENT READER**

## **📌 L'Application**
L'application **AUGMENTED DOCUMENT READER** dispose d'une interface graphique développée avec **Streamlit**, permettant à l'utilisateur d'effectuer l'extraction d'entités nommées à partir de fichiers.

Deux formats sont acceptés : **TXT et DOCX**. L'utilisateur **télécharge un fichier**, et l'algorithme de **NER adapté est automatiquement déclenché**. Le résultat est restitué sous **format JSON**.

Les différents types de NER intégrés sont **testés directement dans le notebook** `named_entity_recognation.ipynb` :
- **Rule-Based NER** (basé sur des règles)
- **Open Source Model-Based NER** (modèle NER pré-entraîné)
- **LLM/RAG-Based NER** (basé sur un modèle de langage et un moteur de recherche sémantique)

Pour le **LLM/RAG-Based NER**, j'ai implémenté un **RAG** en utilisant **Langchain, FAISS et Mistral (via Ollama)** en local.

## **🔹 L'App NER :**
![L'App NER](src/images/app.png)

## **🔹 Extraction des entités basée sur des règles (fichier DOCX) :**
![L'App NER](src/images/v_docx.png)

## **🔹 Extraction des entités avec un modèle NLP (fichier TXT) :**
![L'App NER](src/images/v_txt.png)

---

## **💡 Comment obtenir un modèle NER spécifique aux données financières ?**
On peut **fine-tuner** un modèle NER pré-entraîné sur nos propres données.  

### **1️⃣ Collecte des Données**  
- Rassembler des **documents financiers annotés**.  
- Annoter les entités (**ORG, MONEY, INSTRUMENT, DATE, etc.**) en utilisant la **méthode BIO** par exemple. 
- Nettoyer et prétraiter les données pour un format compatible.  

### **2️⃣ Fine-tuning**  
- Choisir un **modèle NER pré-entraîné** (ex: Hugging Face).  
- Entraîner uniquement la **tête de classification** en **gelant** les premières couches du modèle.  

---

🚀 **L'objectif : un modèle optimisé pour extraire les entités financières avec précision !**
