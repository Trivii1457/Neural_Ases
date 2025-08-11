from pathlib import Path
import os

class Config:
    BASE_DIR = Path(__file__).resolve().parent.parent
    AUDIO_UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads', 'audio')
    PDF_OUTPUT_FOLDER = os.path.join(BASE_DIR, 'outputs', 'pdf')
    
    # Database configuration
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///database.db')
    
    # Logging configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    # AI Model configuration
    MODEL_PATH = os.getenv('MODEL_PATH', os.path.join(BASE_DIR, 'ml', 'model'))
    
    # Other configurations
    MAX_AUDIO_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
    ALLOWED_AUDIO_EXTENSIONS = {'wav', 'mp3', 'm4a', 'flac'}