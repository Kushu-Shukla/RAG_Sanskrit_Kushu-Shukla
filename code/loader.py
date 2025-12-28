from langchain_community.document_loaders import TextLoader, PyMuPDFLoader

def load_document(path: str):
    if path.endswith(".txt"):
        return TextLoader(path, encoding="utf-8").load()
    elif path.endswith(".pdf"):
        return PyMuPDFLoader(path).load()
    else:
        raise ValueError("Only .txt or .pdf Sanskrit documents are supported")
