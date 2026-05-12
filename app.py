#Main Streamlit app

#Handles:

#file upload
#user chat input
#displaying responses

#This becomes your dashboard/UI.

import streamlit as st
import os

from rag.pdf_loader import load_pdf


st.set_page_config(
    page_title="RAG PDF Chatbot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI PDF Chatbot")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)

if uploaded_file is not None:

    # create uploads folder if not exists
    os.makedirs("uploads", exist_ok=True)

    # save uploaded file
    file_path = os.path.join("uploads", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully!")

    # extract text
    text = load_pdf(file_path)

    st.subheader("📜 Extracted Text Preview")

    st.text_area(
        "PDF Content",
        text[:3000],
        height=400
    )