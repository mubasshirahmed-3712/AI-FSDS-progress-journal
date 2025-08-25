"""
Dictionary Utility Functions with gTTS
Author: Mubasshir Ahmed
"""

from nltk.corpus import wordnet
import nltk
from gtts import gTTS
import tempfile

# Ensure WordNet is downloaded
nltk.download('wordnet', quiet=True)

# ---------- Speech ----------
def speak(text: str, lang: str = "en", slow: bool = False):
    """Convert text to speech using gTTS and return temp mp3 path"""
    try:
        tts = gTTS(text=text, lang=lang, slow=slow)
        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(tmp_file.name)
        return tmp_file.name
    except Exception as e:
        print("Speech Error:", e)
        return None

# ---------- Dictionary ----------
def find_synonyms(word: str):
    syn_words = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            syn_words.add(lemma.name())
    return list(syn_words)

def find_antonyms(word: str):
    ant_words = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.antonyms():
                for ant in lemma.antonyms():
                    ant_words.add(ant.name())
    return list(ant_words)

def get_meaning(word: str):
    """Return meanings, synonyms, antonyms as dict"""
    synsets = wordnet.synsets(word)
    if not synsets:
        return {"meanings": [], "synonyms": [], "antonyms": []}

    meanings = [syn.definition() for syn in synsets[:5]]
    synonyms = find_synonyms(word)[:10]
    antonyms = find_antonyms(word)[:10]

    return {"meanings": meanings, "synonyms": synonyms, "antonyms": antonyms}
