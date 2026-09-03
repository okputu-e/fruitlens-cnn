import streamlit as st
from PIL import Image

# Configure the browser page
st.set_page_config(
    page_title="FruitLens",
    page_icon="🍎"
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
        width="stretch"
    )

    # The CNN model will be connected here later
    if st.button("Classify Fruit"):
        st.info("The CNN model has not been connected yet.")