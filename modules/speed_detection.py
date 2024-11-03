def calculate_speed(distance, time):
    # Speed = Distance / Time
    if time == 0:
        return 0
    speed = distance / time  # Speed in meters per second
    return speed
from logger import speed_detection_logger

def calculate_speed(distance, time):
    try:
        speed_detection_logger.info("Calculating speed.")
        if time > 0:
            speed = (distance / time) * 3.6  # Convert m/s to km/h
            speed_detection_logger.info(f"Speed calculated: {speed} km/h.")
            return speed
        else:
            speed_detection_logger.warning("Time must be greater than 0 to calculate speed.")
            return 0
    except Exception as e:
        speed_detection_logger.error(f"Error calculating speed: {e}")
