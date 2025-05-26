import streamlit as st
import os
from dotenv import load_dotenv
from utils import *


load_dotenv()

def main():
    st.set_page_config(page_title="PDF Summarizer")
    st.title("PDF Summarizer")
    st.write("Upload a PDF file to get a summary.")
    st.divider()
    
    pdf=st.file_uploader("Upload PDF", type=["pdf"])
    submit=st.button("Summarize")

    

    if submit:
        response = summarize_text(pdf)

        st.subheader("Summary")
        st.write(response)

if __name__ == "__main__":
    main()