from fastapi import APIRouter, UploadFile, File, HTTPException
from src.models.predict import predict_image
import os
import shutil

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.get("/health")
def health():
    return {
        "status": "Backend Working"
    }


@router.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Check if uploaded file is an image
    if file.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
        raise HTTPException(
            status_code=400,
            detail="Please upload a JPG or PNG image."
        )

    # Save uploaded image
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Call Person 2's prediction function
    result = predict_image(file_path)

    # Send prediction back
    return {
        "filename": file.filename,
        "prediction": result
    }
