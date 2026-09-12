import streamlit as st
from PIL import Image

# Configure the browser page
st.set_page_config(
    page_title="FruitLens",
    page_icon="🍎"
)

# Increase font sizes
st.markdown(
    """
    <style>

    [data-testid="stMainBlockContainer"] {
    padding-top: 3rem !important;
}
    p {
        font-size: 18px !important;
    }

    [data-testid="stFileUploader"] label {
        font-size: 18px !important;
    }

    .stButton button {
        font-size: 16px !important;
        padding: 8px 18px;
    }

    [data-testid="stAlert"] p {
        font-size: 16px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Application heading
st.title("🍎 FruitLens 🍌")
st.write("Upload a photo of an apple or banana.")

# Allow the user to upload an image
uploaded_file = st.file_uploader(
    "Choose a fruit image",
    type=["jpg", "jpeg", "png"]
)

# Continue only after an image has been uploaded
if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(
        image,
        caption="Uploaded image",
        width=250
    )

    # The CNN model will be connected here later
    if st.button("Classify Fruit"):
        st.info("The CNN model has not been connected yet.")
