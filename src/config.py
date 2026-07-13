from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME = "Explainable Chest X-ray Triage API"
    MODEL_PATH = "models/bestmodel.pth"
    LABEL_MAP_PATH = "models/labelmap.json"
    IMAGE_SIZE = 224
    DEVICE = "cpu"
    UPLOAD_FOLDER = "uploads"

settings = Settings()
