import streamlit as st

st.set_page_config(
    page_title="LungLens AI",
    page_icon="🫁",
    layout="wide"
)

st.title("🫁 LungLens AI")
st.subheader("Chest X-ray Disease Detection")

st.write(
    """
    Upload a Chest X-ray image to detect whether it is
    **BACTERIA** or **VIRUS** using a trained ResNet18 model.
    """
)

uploaded_file = st.file_uploader(
    "Upload Chest X-ray",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.success("Image uploaded successfully!")
