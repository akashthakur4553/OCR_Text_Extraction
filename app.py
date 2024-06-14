import streamlit as st
from PIL import Image
from pytesseract import image_to_string

import pytesseract

# Configure the path to Tesseract
pytesseract.pytesseract.tesseract_cmd = "Tesseract-OCR/tesseract.exe"

st.set_page_config(layout="wide")


def main():
    st.title("OCR Text Extraction")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        if st.button("Extract Text"):
            # Extract text from image
            extracted_text = image_to_string(img)

            # Display extracted text
            st.subheader("Extracted Text")
            st.text_area(
                label="Extracted Text Area",
                value=extracted_text,
                height=200,
                label_visibility="collapsed",
            )


if __name__ == "__main__":
    main()
