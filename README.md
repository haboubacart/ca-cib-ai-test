### L'application
L'application AUGMENTED DOCUMENT READER dispose d'une interface graphique (streamlit) via laquelle l'utilisateur peut réaliser l'extraction d'entités nommées, à partir de fichier.
Deux formats sont acceptés : txt et docx. L'utilisateur upload un fichier de son choix et aussitôt est déclenché l'algorithme de NER adapté. Le résultat est rendu sous format json.
L'ensemble des différents types de NER proposés sont testés diretement dans le notebook named_entity_recognation.ipynb, à savoir : rules based NER, open source model based NER et LLM/RAG based NER. Pour le dernier type, j'ai implémenté un RAG en utilisant langchain, FAISS et Mistral comme LLM via ollama en local.

#### L'App NER :
![L'App NER](src/images/app.png)

#### L'extraction des entités basée sur des règles (fichier docx) :
![L'App NER](src/images/v_docx.png)

#### L'extraction des entités avec un modèle NLP (fichier txt) :
![L'App NER](src/images/v_txt.png)

### Comment avoir un modèle NER spécifique pour les données financières ?
On peut fine-tuner une modèle NER pre-entrainé sur nos propres données. Les étapes à suivre :
#### Collecte des Données  
- Rassembler des documents financiers annotés 
- Annoter les entités (ORG, MONEY, INSTRUMENT, DATE, etc.) en utilisant la methode BIO par exemple
- Nettoyage et prétraitement des données

#### Fine-tuning
- Choisir un modèle NER pré-entrainer sur HF par exemple et entrainer que la tête de classification (freeze les premières couches)

