from flask import Blueprint, request, jsonify
from modules.tracking import track_vehicle  # Import your tracking function

tracking_bp = Blueprint('tracking', __name__)

@tracking_bp.route('/track_vehicle', methods=['POST'])
def track_vehicle_route():
    vehicle_id = request.json.get('vehicle_id')
    location_info = track_vehicle(vehicle_id)  # Call your tracking function
    return jsonify(location_info), 200
