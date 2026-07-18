import streamlit as st
import requests

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

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        files=files
    )

    if response.status_code == 200:
       result = response.json()

       prediction = result["prediction"]

       st.subheader("Prediction")

       st.success(f"Disease: {prediction[0]}")
       st.write(f"Confidence: {prediction[1] * 100:.2f}%")
    else:
        st.error("Prediction failed.")