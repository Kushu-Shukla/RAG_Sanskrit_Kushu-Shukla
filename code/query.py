query = input("प्रश्नं लिखत: ")

if any(c.isascii() for c in query):
    query = iast_to_devanagari(query)

answer = run_rag(query, index, chunks, model)
print("उत्तरम्:", answer)
