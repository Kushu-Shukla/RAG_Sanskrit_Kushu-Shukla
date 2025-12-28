import numpy as np

def retrieve(query, index, chunks, embedder, top_k=8):
    query_embedding = embedder.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)

    results = []
    for i in indices[0]:
        results.append(chunks[i].page_content)

    return results
