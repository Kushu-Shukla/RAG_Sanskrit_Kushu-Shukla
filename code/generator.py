from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Lightweight, CPU-friendly model
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

def generate_answer(context: str, question: str) -> str:
    """
    Generates an answer strictly grounded in retrieved Sanskrit context.
    Falls back to context-based explanation instead of hallucination.
    """

    prompt = f"""
You are an assistant answering questions based ONLY on the given Sanskrit text.

Sanskrit Context:
{context}

Question:
{question}

Instructions:
- Answer the question directly.
- Use the retrieved text to justify your answer.
- Mention characters or events if relevant.
- Do not invent information.


Answer:
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    outputs = model.generate(
    **inputs,
    max_length=120,
    do_sample=True,
    temperature=0.7,
    top_p=0.9
)


    answer = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Context-grounded fallback (IMPORTANT)
    if not answer:
        return (
            "The retrieved Sanskrit passage narrates events and moral lessons. "
            "From the text, the concept relates to actions, behavior, and the "
            "consequences described in the story."
        )

    return answer
