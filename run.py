import spacy
import streamlit as st

from spacy import displacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Use the current text from your text area
text = st.session_state.get('text_area', '')

if text.strip():
    doc = nlp(text)

    # Display entities with colors using displaCy HTML
    html = displacy.render(doc, style="ent", jupyter=False)
    st.write("**Detected Entities:**", unsafe_allow_html=True)
    st.markdown(html, unsafe_allow_html=True)

    # Optional: show entity table
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    if entities:
        st.markdown("**Entity Table:**")
        st.table(entities)
    else:
        st.info("No named entities found.")

else:
    st.info("Paste or select some text to see NER results.")
