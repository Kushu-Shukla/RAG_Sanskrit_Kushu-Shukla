import re
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def clean_sanskrit(text: str) -> str:
    text = re.sub(r"[^\u0900-\u097F\s]", "", text)
    return re.sub(r"\s+", " ", text).strip()

def iast_to_devanagari(text: str) -> str:
    return transliterate(text, sanscript.IAST, sanscript.DEVANAGARI)
