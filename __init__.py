# app/__init__.py

from flask import Flask

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Folder to save uploaded files
app.secret_key = "95188ce94ae88709b34aadfd2820adb4"  # Change this to a strong secret key in production

# Import and register blueprints (optional)
from .routes.index import index_bp
from .routes.helmet_route import helmet_bp
from .routes.number_plate_route import number_plate_bp
# Add other blueprints as needed

app.register_blueprint(index_bp)
app.register_blueprint(helmet_bp)
app.register_blueprint(number_plate_bp)
# Register other blueprints as needed

# Ensure the upload folder exists
import os
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Import modules if necessary
import app.modules.model_loader
