def run_rag(query, index, chunks, embed_model):
    context = retrieve(query, index, chunks, embed_model)
    return generate(" ".join(context), query)
