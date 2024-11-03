# app/modules/__init__.py

# Import specific functions for direct access from modules
from app.modules.model_loader import detect_helmet, recognize_number_plate, calculate_speed, detect_occupants
from app.modules.vehicle_classification import classify_vehicle
from app.modules.incident_detection import detect_incident
from app.modules.traffic_flow_analysis import analyze_traffic_flow
from app.modules.driver_behavior import detect_aggressive_driving
from app.modules.alerts_notifications import send_alert
from app.modules.database_handler import get_vehicle_info
from app.modules.dashboard_analytics import generate_analytics_data
