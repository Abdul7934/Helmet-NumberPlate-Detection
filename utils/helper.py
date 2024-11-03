import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os

def draw_bounding_box(frame, bbox, label, color=(0, 255, 0)):
    """
    Draws a bounding box around detected objects.
    
    Args:
        frame: The frame on which to draw.
        bbox: The bounding box coordinates (x, y, width, height).
        label: The label to display.
        color: The color of the bounding box (default is green).
    """
    x, y, w, h = bbox
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
    cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

def calculate_speed(distance, time):
    """
    Calculates the speed given distance and time.
    
    Args:
        distance: The distance traveled (in meters).
        time: The time taken (in seconds).
        
    Returns:
        Speed in kilometers per hour (km/h).
    """
    if time > 0:
        speed = (distance / time) * 3.6  # Convert m/s to km/h
        return speed
    return 0

def load_model(model_path):
    """
    Loads a trained machine learning model from a specified path.
    
    Args:
        model_path: The path to the model file.
        
    Returns:
        Loaded model.
    """
    try:
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at path: {model_path}")
        
        model = load_model(model_path)
        return model
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        return None
