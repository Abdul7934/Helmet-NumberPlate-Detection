from flask import Blueprint, request, jsonify
from modules.helmet_detection import detect_helmet  # Import your helmet detection function

helmet_bp = Blueprint('helmet', __name__)

@helmet_bp.route('/detect_helmet', methods=['POST'])
def detect_helmet_route():
    video_path = request.json.get('video_path')
    results = detect_helmet(video_path)  # Call your detection function
    return jsonify(results), 200
