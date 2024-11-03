from flask import Blueprint, render_template, request
import os

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def home():
    return render_template('index.html')  # Render the main page

@index_bp.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return 'No video uploaded', 400
    
    video_file = request.files['video']
    if video_file.filename == '':
        return 'No selected video', 400
    
    save_path = os.path.join('uploads', video_file.filename)
    video_file.save(save_path)
    
    return 'Video uploaded successfully', 200
