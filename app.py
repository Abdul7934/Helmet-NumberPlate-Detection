from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

# Import custom modules from app/models
from app.modules.model_loader import detect_helmet, recognize_number_plate, calculate_speed, detect_occupants
# ... [Other imports remain unchanged]

from app.modules.vehicle_classification import classify_vehicle
from app.modules.incident_detection import detect_incident
from app.modules.traffic_flow_analysis import analyze_traffic_flow
from app.modules.driver_behavior import detect_aggressive_driving
from app.modules.alerts_notifications import send_alert
from app.modules.database_handler import get_vehicle_info
from app.modules.dashboard_analytics import generate_analytics_data

# Import utilities from utils/
from utils.preprocessor import preprocess_video
from utils.constants import VIDEO_THRESHOLD, IMAGE_THRESHOLD
from utils.helper import format_detection_result

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Folder to save uploaded files
app.secret_key = "your_secret_key"  # Change this to a strong secret key in production

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Allowed file extensions
ALLOWED_EXTENSIONS = {'mp4', 'mov', 'avi', 'jpg', 'jpeg', 'png'}

# Utility function to check file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Register blueprints from routes/
from routes.index import index_bp
from routes.helmet_route import helmet_bp
from routes.number_plate_route import number_plate_bp
from routes.speed_route import speed_bp
from routes.violation_alert_route import violation_alert_bp
from routes.analytics_route import analytics_bp
from routes.tracking_route import tracking_bp
from routes.occupancy_route import occupancy_bp

# Registering blueprints
app.register_blueprint(index_bp)
app.register_blueprint(helmet_bp)
app.register_blueprint(number_plate_bp)
app.register_blueprint(speed_bp)
app.register_blueprint(violation_alert_bp)
app.register_blueprint(analytics_bp)
app.register_blueprint(tracking_bp)
app.register_blueprint(occupancy_bp)

# Routes

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            flash('File uploaded successfully')
            return redirect(url_for('index'))  # Change 'index' to the correct endpoint

    return render_template('upload.html')

@app.route('/helmet_detection')
def helmet_detection():
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], 'test_video.mp4')  # Adjust as necessary
    helmet_result = detect_helmet(video_path)
    return render_template('helmet_detection.html', result=helmet_result)

@app.route('/number_plate_detection')
def number_plate_detection():
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'test_image.jpg')  # Adjust as necessary
    plate_result = recognize_number_plate(image_path)
    return render_template('number_plate_detection.html', result=plate_result)

@app.route('/speed_detection')
def speed_detection():
    distance = 100  # Example distance in meters
    time = 5  # Example time in seconds
    speed_result = calculate_speed(distance, time)
    return render_template('speed_detection.html', result=speed_result)

@app.route('/occupancy_detection')
def occupancy_detection():
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'test_image.jpg')  # Adjust as necessary
    occupants_result = detect_occupants(image_path)
    return render_template('occupancy_detection.html', result=occupants_result)

@app.route('/alert_violation')
def alert_violation():
    message = "Traffic violation detected"
    alert_result = send_alert(message)
    return render_template('alert_violation.html', result=alert_result)

@app.route('/analytics')
def analytics():
    analytics_data = generate_analytics_data()
    return render_template('analytics.html', data=analytics_data)

@app.route('/vehicle_tracking')
def vehicle_tracking():
    vehicle_info = get_vehicle_info("ABC123")  # Replace with actual logic to get vehicle info
    return render_template('vehicle_tracking.html', info=vehicle_info)

@app.route('/incident_detection')
def incident_detection():
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], 'test_video.mp4')  # Adjust as necessary
    incident_result = detect_incident(video_path)
    return render_template('incident_detection.html', result=incident_result)

@app.route('/traffic_flow_analysis')
def traffic_flow_analysis():
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], 'traffic_video.mp4')  # Adjust as necessary
    traffic_data = analyze_traffic_flow(video_path)
    return render_template('traffic_flow_analysis.html', data=traffic_data)

@app.route('/driver_behavior')
def driver_behavior():
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], 'test_video.mp4')  # Adjust as necessary
    behavior_result = detect_aggressive_driving(video_path)
    return render_template('driver_behavior.html', result=behavior_result)

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
