from flask import Blueprint, request, jsonify
from modules.number_plate_detection import recognize_plate  # Import your number plate detection function

number_plate_bp = Blueprint('number_plate', __name__)

@number_plate_bp.route('/detect_plate', methods=['POST'])
def detect_plate_route():
    video_path = request.json.get('video_path')
    plate_info = recognize_plate(video_path)  # Call your recognition function
    return jsonify(plate_info), 200
