from code.loader import load_document
from code.preprocess import iast_to_devanagari
from code.indexer import build_index
from code.retriever import retrieve
from code.generator import generate_answer

DOC_PATH = "data/bhagvada_gita.txt"

print(" Loading Sanskrit documents...")
documents = load_document(DOC_PATH)
print(f"✅ Loaded {len(documents)} document(s)")

print("🔎 Building vector index (CPU only)...")
index, chunks, embedder = build_index(documents)
print(f"✅ Index built with {len(chunks)} chunks")

print("\n Sanskrit RAG System Ready")
print("Type your question in Sanskrit or IAST")
print("Type 'exit' to quit\n")

while True:
    query = input("प्रश्नः: ").strip()

    if query.lower() == "exit":
        print(" Exiting.")
        break

    # 🔹 Normalize common mixed-language inputs
    q = query.lower()
    q = q.replace("kim asti", "किम् अस्ति")
    q = q.replace("karma", "कर्म")
    q = q.replace("dharma", "धर्म")
    q = q.replace("bhakta", "भक्त")

    # 🔹 Convert remaining ASCII to Devanagari
    # Convert ONLY if query contains Latin letters
    if any(c.isalpha() and c.isascii() for c in q):
        q = iast_to_devanagari(q)


    # 🔹 Retrieve context
    contexts = retrieve(q, index, chunks, embedder, top_k=8)

    print("\n Retrieved Context (preview):")
    for i, c in enumerate(contexts, 1):
        print(f"[{i}] {c[:120]}...")

    print("\n Generating answer (CPU, please wait)...")
    answer = generate_answer("\n".join(contexts), q)

    # 🔹 Generate answer
    answer = generate_answer("\n".join(contexts), q)

    print("\nउत्तरम्:")
    print(answer)
    print("-" * 60)
