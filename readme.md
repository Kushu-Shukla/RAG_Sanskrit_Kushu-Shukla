
---

#  Sanskrit Document Retrieval-Augmented Generation (RAG) System (CPU-Only)

##  Project Overview

This project implements an **end-to-end Retrieval-Augmented Generation (RAG) system** for **Sanskrit documents**, designed to operate **entirely on CPU** using open-source tools.

The system ingests Sanskrit text, preprocesses and indexes it for retrieval, and generates context-grounded answers to user queries written in **Sanskrit or transliterated (IAST) form**.
The architecture strictly follows **RAG best practices**, with a clean separation between retrieval and generation components.

---

##  Objectives

* Ingest Sanskrit documents (`.txt` or `.pdf`)
* Preprocess and chunk Sanskrit text
* Index documents for semantic retrieval
* Accept user queries in Sanskrit or IAST
* Retrieve relevant Sanskrit context
* Generate grounded answers using a CPU-based LLM
* Avoid hallucination through context-aware generation
* Maintain modular, reproducible, and transparent design

---

##  System Architecture

```
User Query
   │
   ▼
Query Normalization & Transliteration
   │
   ▼
Retriever (FAISS + Sentence Transformers)
   │
   ▼
Relevant Sanskrit Chunks
   │
   ▼
Generator (FLAN-T5, CPU-Only)
   │
   ▼
Grounded Answer
```

The system ensures:

* Clear retriever–generator separation
* Explicit visibility of retrieved context
* No black-box components

---

##  Project Structure

```
RAG_Sanskrit_<InternName>/
│
├── code/
│   ├── loader.py        # Sanskrit document loader
│   ├── preprocess.py   # Transliteration & normalization
│   ├── indexer.py      # Chunking + vector index creation
│   ├── retriever.py    # Semantic retrieval (FAISS)
│   ├── generator.py    # CPU-based answer generation
│   ├── main.py         # Interactive RAG pipeline
│   └── __init__.py
│
├── data/
│   └── bhagvada_gita.txt   # Sanskrit corpus (sample)
│
├── report/
│   └── final_report.pdf   # Technical report
│
├── Dockerfile             # CPU-only container
├── requirements.txt       # Python dependencies
└── README.md
```

---

##  Sanskrit Corpus

* Language: **Pure Sanskrit (Devanagari)**
* Format: `.txt`
* Nature:

  * Narrative stories
  * Moral and philosophical teachings
  * Classical Sanskrit prose and verses

 The corpus is **narrative**, not dictionary-style, which influences answer style (contextual summaries rather than strict definitions).

---

## ⚙️ Technologies Used

| Component       | Tool                                                          |
| --------------- | ------------------------------------------------------------- |
| Embedding Model | `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` |
| Vector Store    | FAISS (CPU)                                                   |
| LLM             | `google/flan-t5-base`                                         |
| Transliteration | `indic-transliteration`                                       |
| Frameworks      | Hugging Face, LangChain (community modules)                   |
| Deployment      | Local / Docker (CPU-only)                                     |

---

##  Setup Instructions (Local)

### 1️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the system

```bash
python -m code.main
```

---

##  Sample Queries

### Sanskrit

```
मूर्खभृत्यस्य कथायाः शिक्षाः काः?
शंखनादः किमर्थं मूर्खः?
```

### IAST / Transliteration

```
karma kim asti
dharma kim
```

---

##  Output Behavior (Important)

* Retrieved Sanskrit passages are **explicitly displayed**
* Answers are **grounded in retrieved context**
* If the text does not explicitly define a concept, the system **summarizes implications**
* Hallucination is intentionally avoided

This behavior is **by design** and aligns with responsible RAG practices.

---

## ⏱ Performance Notes

* Index creation: ~1–2 seconds (small corpus)
* Retrieval: < 100 ms
* Generation: 5–15 seconds (CPU-only, expected)
* Memory: Suitable for low-resource systems

---

##  Docker (CPU-Only)

### Build image

```bash
docker build -t rag-sanskrit .
```

### Run container

```bash
docker run -it rag-sanskrit
```

The Docker image:

* Uses CPU-only dependencies
* Contains no GPU / CUDA components
* Is lightweight and reproducible

---

##  Design Decisions & Justification

* **CPU-only models** were chosen to meet constraints
* **Context-first answers** prevent hallucination
* Narrative Sanskrit texts favor **explanatory summaries**
* Transparency in retrieval improves trust and evaluation clarity

---

##  Known Limitations

* Sanskrit generation quality depends on lightweight models
* Narrative texts limit definition-style answers
* Larger corpora would improve retrieval diversity

These are **acknowledged and documented design trade-offs**.

---

##  Future Enhancements

* Larger Sanskrit datasets
* Sanskrit-native Indic LLMs
* Persistent vector storage
* Web-based query interface

---

##  Submission Checklist

* ✔ Complete runnable code
* ✔ Sanskrit-only data
* ✔ CPU-only inference
* ✔ Modular RAG design
* ✔ Technical report included
* ✔ Docker support

---

## 📄 License

This project uses only **open-source libraries** and is intended for **educational and research purposes**.

---

### 🎉 Status: **Placement-Ready Submission**

---
