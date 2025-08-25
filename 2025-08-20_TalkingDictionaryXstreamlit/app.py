"""
Streamlit Dictionary App with Auto-Voice (gTTS)
Author: Mubasshir Ahmed
"""

import streamlit as st
from dictionary_utils import get_meaning, speak
import base64

# ------------------- PAGE CONFIG -------------------
st.set_page_config(
    page_title="Mubasshir's Talking Dictionary",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------- CUSTOM CSS -------------------
st.markdown("""
<style>
.big-title {
    font-size:40px !important;
    color: #9370DB;
    font-weight: bold;
    text-align: center;
}
.section-title {
    font-size:22px !important;
    font-weight:bold;
    color: #9370DB;
    margin-top:20px;
}
.result-box {
    background-color: #1e1e1e;
    padding: 15px;
    border-radius: 10px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# ------------------- APP TITLE -------------------
st.markdown("<div class='big-title'>📖 Mubasshir's Pro Talking Dictionary</div>", unsafe_allow_html=True)
st.write("### 👋 Enter a word to find its **meanings, synonyms, and antonyms.**")

# ------------------- SIDEBAR -------------------
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    lang = st.selectbox("Voice Language", ["en", "en-uk", "en-us", "en-in"])
    slow_voice = st.checkbox("Slow voice", value=False)

    st.markdown("## 📜 Search History")
    if "history" not in st.session_state:
        st.session_state["history"] = []
    if st.session_state["history"]:
        for h in st.session_state["history"]:
            st.write("- " + h)
    else:
        st.write("No history yet.")

# ------------------- INPUT -------------------
word = st.text_input("🔎 Enter a word", "")

# ------------------- PROCESS -------------------
if st.button("Get Meaning"):
    if word.strip():
        result = get_meaning(word.strip())

        # Add to history
        if word not in st.session_state["history"]:
            st.session_state["history"].insert(0, word)
            st.session_state["history"] = st.session_state["history"][:10]

        # Display results
        st.markdown("<div class='section-title'>📘 Meanings</div>", unsafe_allow_html=True)
        if result["meanings"]:
            for i, m in enumerate(result["meanings"], 1):
                st.markdown(f"<div class='result-box'>{i}. {m}</div>", unsafe_allow_html=True)
        else:
            st.error("No meanings found.")

        st.markdown("<div class='section-title'>✨ Synonyms</div>", unsafe_allow_html=True)
        if result["synonyms"]:
            st.markdown(f"<div class='result-box'>{', '.join(result['synonyms'])}</div>", unsafe_allow_html=True)
        else:
            st.warning("No synonyms found.")

        st.markdown("<div class='section-title'>❌ Antonyms</div>", unsafe_allow_html=True)
        if result["antonyms"]:
            st.markdown(f"<div class='result-box'>{', '.join(result['antonyms'])}</div>", unsafe_allow_html=True)
        else:
            st.info("No antonyms found.")

        # Speak full text
        full_text = "Meanings: " + " ; ".join(result["meanings"])
        if result["synonyms"]:
            full_text += " . Synonyms: " + ", ".join(result["synonyms"])
        if result["antonyms"]:
            full_text += " . Antonyms: " + ", ".join(result["antonyms"])

        audio_file = speak(full_text, lang=lang, slow=slow_voice)

        if audio_file:
            # Convert file to base64
            with open(audio_file, "rb") as f:
                audio_bytes = f.read()
            b64 = base64.b64encode(audio_bytes).decode()
            md = f"""
            <audio autoplay>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
            st.markdown(md, unsafe_allow_html=True)

    else:
        st.warning("⚠️ Please enter a word first.")
