from flask import Blueprint, request, jsonify
from modules.alerts_notifications import send_alert  # Import your alert function

violation_alert_bp = Blueprint('violation_alert', __name__)

@violation_alert_bp.route('/send_alert', methods=['POST'])
def send_alert_route():
    violation_details = request.json
    success = send_alert(violation_details)  # Call your alert function
    return jsonify({'status': 'alert sent' if success else 'failed to send alert'}), 200
