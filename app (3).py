import streamlit as st

st.set_page_config(page_title="IKC Studio", layout="wide")

st.title("IKC Studio")
st.write("Turn your content into a smart AI prompt (no API needed)")

# Upload file
uploaded_file = st.file_uploader("Upload your file", type=["txt"])

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")

    st.subheader("Extracted Content")
    st.text_area("Content", text, height=200)

    # Generate prompt
    prompt = f"""
You are an expert educator and curriculum designer.

Analyze the following content and generate:
1. Key themes
2. Learning objectives
3. Suggested activities
4. Assessment ideas

Content:
{text}
"""

    st.subheader("Prompt for Claude")
    st.code(prompt)

    st.info("Copy this prompt and paste it into Claude.")
