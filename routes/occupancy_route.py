from flask import Blueprint, request, jsonify
from modules.occupancy_detection import detect_occupancy  # Import your occupancy detection function

occupancy_bp = Blueprint('occupancy', __name__)

@occupancy_bp.route('/detect_occupancy', methods=['POST'])
def detect_occupancy_route():
    video_path = request.json.get('video_path')
    occupancy_info = detect_occupancy(video_path)  # Call your occupancy detection function
    return jsonify(occupancy_info), 200
