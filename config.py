import os

class Config:
    # General configurations
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_default_secret_key')  # Change this for production
    DEBUG = os.environ.get('FLASK_DEBUG', 'True') == 'True'  # Enable debug mode

    # File upload settings
    UPLOAD_FOLDER = 'uploads'  # Folder where uploaded files will be saved
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Maximum file size (16MB)

    # Database settings (example for SQLite, adjust as needed)
    DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///your_database.db')

    # Other settings
    HELMET_DETECTION_MODEL_PATH = os.environ.get('HELMET_MODEL_PATH', 'models/helmet_detection_model.h5')
    NUMBER_PLATE_MODEL_PATH = os.environ.get('PLATE_MODEL_PATH', 'models/number_plate_recognition_model.h5')
    ALERTS_API_KEY = os.environ.get('ALERTS_API_KEY', 'your_alerts_api_key')  # Example for Twilio or similar services

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# You can define a method to get the appropriate configuration based on the environment
def get_config():
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'production':
        return ProductionConfig
    return DevelopmentConfig
