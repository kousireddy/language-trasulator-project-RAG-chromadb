import streamlit as st
from datetime import datetime
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="",
    layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

#MainMenu,
footer,
header {
    visibility: hidden;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2.5rem;
    max-width: 1400px;
}

.stApp {
    background: linear-gradient(180deg, #eef2ff 0%, #f8fafc 100%);
}

.hero {
    background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);
    padding: 42px 36px;
    border-radius: 28px;
    text-align: center;
    color: white;
    margin-bottom: 32px;
    box-shadow: 0 14px 38px rgba(79, 70, 229, 0.18);
}

.hero-title {
    font-size: 54px;
    font-weight: 800;
    margin-bottom: 10px;
}

.hero-subtitle {
    font-size: 18px;
    opacity: 0.95;
    line-height: 1.6;
}

.section-card,
.card {
    background: white;
    padding: 26px;
    border-radius: 22px;
    box-shadow: 0 8px 28px rgba(15, 23, 42, 0.08);
}

.stats-card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 6px 18px rgba(15, 23, 42, 0.08);
}

.result-box,
.history-card,
.sidebar-box {
    background: white;
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0 6px 20px rgba(15, 23, 42, 0.06);
}

.result-box {
    border-left: 6px solid #4F46E5;
    line-height: 1.8;
    white-space: pre-wrap;
}

.history-card {
    margin-bottom: 14px;
    border-left: 5px solid #7C3AED;
}

.sidebar-box {
    border: 1px solid #E5E7EB;
}

.stTextArea textarea,
.stTextInput input {
    border-radius: 16px !important;
    border: 2px solid #E5E7EB !important;
    font-size: 16px !important;
}

.stButton > button {
    width: 100%;
    height: 56px;
    border-radius: 16px;
    border: none;
    background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);
    color: white;
    font-size: 18px;
    font-weight: 700;
}

.stButton > button:hover {
    opacity: 0.92;
}

.st-badge {
    color: #4F46E5;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# SESSION STATE
# ==================================================

if "history" not in st.session_state:
    st.session_state.history = []

# ==================================================
# HEADER
# ==================================================

st.markdown(
    """
<div class="hero">
    <div class="hero-title">AI Language Translator</div>
    <div class="hero-subtitle">
        Translate text into any language instantly using Groq + LangChain.
        Preserve meaning, formatting
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:
    st.markdown("""
### How to use

1. Paste text or document content.
2. Enter a target language.
3. Click **Translate Text**.
4. Download or review translations below.
""")
    st.markdown("""
<div class="sidebar-box">
<b>Example languages:</b><br>
French, Spanish, Hindi, Chinese, Arabic, German, Telugu
</div>
""", unsafe_allow_html=True)

# ==================================================
# INPUT SECTION
# ==================================================

with st.form("translation_form"):
    left, right = st.columns([3, 1], gap="large")

    with left:
        text = st.text_area(
            "Paste your text",
            height=360,
            placeholder="Paste article, email, document, or paragraph here...",
        )

    with right:
        target_language = st.text_input(
            "Target language",
            placeholder="Telugu",
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.metric("Characters", len(text))
        st.metric("Words", len(text.split()))

        estimated_minutes = max(1, int(len(text.split()) / 180)) if text else 0
        st.metric("Estimated reading time", f"{estimated_minutes} min")

    translate = st.form_submit_button("Translate Text")

# ==================================================
# TRANSLATION
# ==================================================

if translate:
    if not text.strip():
        st.warning("Please enter the text you want to translate.")
    elif not target_language.strip():
        st.warning("Please enter a target language.")
    else:
        llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

        prompt = ChatPromptTemplate.from_template(
            """
You are an expert translator.

Translate the given text into {target_language}.

Rules:
- Preserve meaning exactly.
- Preserve names.
- Preserve formatting.
- Preserve technical terms.
- Return only translated text.
- Do not explain.

Text:

{text}
"""
        )

        chain = prompt | llm | StrOutputParser()

        with st.spinner(f"Translating to {target_language}..."):
            result = chain.invoke({"target_language": target_language, "text": text})

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.history.insert(
            0,
            {
                "language": target_language,
                "input": text,
                "output": result,
                "timestamp": timestamp,
            },
        )

        st.markdown("---")
        st.subheader("Translation Result")

        result_left, result_right = st.columns([1, 1], gap="large")
        result_left.markdown(
            """
<div class="result-box">
<b>Original Text</b>
<br><br>
""" + text + """
</div>
""",
            unsafe_allow_html=True,
        )
        result_right.markdown(
            """
<div class="result-box">
<b>Translated Text</b>
<br><br>
""" + result + """
</div>
""",
            unsafe_allow_html=True,
        )

        with result_right:
            st.markdown("<div style='margin-top: 16px;'></div>", unsafe_allow_html=True)
            st.download_button(
                label="Download Translation",
                data=result,
                file_name="translation.txt",
                mime="text/plain",
            )

# ==================================================
# HISTORY
# ==================================================

if st.session_state.history:
    st.markdown("---")
    st.subheader("Translation History")

    for item in st.session_state.history:
        with st.expander(f"{item['language']} • {item['timestamp']}"):
            st.markdown(
                """
<div class="history-card">
<b>Target Language:</b> {language}<br>
<b>Created:</b> {timestamp}<br><br>
<b>Original Text</b><br>
{text}<br><br>
<b>Translated Text</b><br>
{output}
</div>
""".
                format(
                    language=item["language"],
                    timestamp=item["timestamp"],
                    text=item["input"],
                    output=item["output"],
                ),
                unsafe_allow_html=True,
            )

