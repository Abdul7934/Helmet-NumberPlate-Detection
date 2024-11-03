from flask import Blueprint, request, jsonify
from modules.speed_detection import calculate_speed  # Import your speed calculation function

speed_bp = Blueprint('speed', __name__)

@speed_bp.route('/calculate_speed', methods=['POST'])
def calculate_speed_route():
    distance = request.json.get('distance')
    time = request.json.get('time')
    speed = calculate_speed(distance, time)  # Call your speed calculation function
    return jsonify({'speed_kmh': speed}), 200
