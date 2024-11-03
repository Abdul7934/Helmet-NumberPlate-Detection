import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class ModelLoader:
    def __init__(self, model_paths):
        """
        Initializes the ModelLoader with paths to models.
        
        Args:
            model_paths (dict): A dictionary containing model names as keys and paths as values.
        """
        self.models = {}
        for model_name, model_path in model_paths.items():
            self.load_model(model_name, model_path)

    def load_model(self, model_name, model_path):
        """
        Loads a model from the specified path and stores it in the models dictionary.
        
        Args:
            model_name (str): Name of the model.
            model_path (str): Path to the model file.
        """
        if os.path.isfile(model_path):  # Use isfile to check for a file
            self.models[model_name] = load_model(model_path)
            print(f"{model_name} loaded successfully from {model_path}.")
        else:
            raise FileNotFoundError(f"Model file {model_path} not found. Please check the path.")

    def get_model(self, model_name):
        """
        Retrieves the loaded model by name.
        
        Args:
            model_name (str): The name of the model to retrieve.
        
        Returns:
            The loaded model if found, otherwise raises KeyError.
        """
        if model_name in self.models:
            return self.models[model_name]
        else:
            raise KeyError(f"Model {model_name} not found.")

# Model paths (update these paths to your actual model files)
model_paths = {
    'helmet_detection': os.path.abspath('app/models/helmet_detection_model.h5'),
    'number_plate_recognition': os.path.abspath('app/models/number_plate_recognition_model.h5'),
    'speed_detection': os.path.abspath('app/models/speed_detection_model.h5'),
    'occupancy_detection': os.path.abspath('app/models/occupancy_detection_model.h5')
}

# Initialize the ModelLoader with model paths
try:
    model_loader = ModelLoader(model_paths)
except FileNotFoundError as e:
    print(e)
    exit()  # Exit if models can't be loaded

# Function for helmet detection
def detect_helmet(video):
    """
    Detects helmet from video frames using the helmet detection model.
    
    Args:
        video: Input video file or frames
    
    Returns:
        Detection result
    """
    helmet_model = model_loader.get_model('helmet_detection')
    # Here, add your video processing logic
    return "Helmet detection result"

# Function for number plate recognition
def recognize_number_plate(image_path):
    """
    Recognizes the number plate from an image.
    
    Args:
        image_path (str): Path to the image file.
        
    Returns:
        Recognition result
    """
    number_plate_model = model_loader.get_model('number_plate_recognition')
    img = image.load_img(image_path, target_size=(224, 224))  # Adjust size as per your model
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = number_plate_model.predict(img_array)
    return "Recognized number plate"

# Function for speed detection
def calculate_speed(distance, time):
    """
    Calculates speed based on distance and time.
    
    Args:
        distance (float): Distance covered
        time (float): Time taken
        
    Returns:
        Speed (float)
    """
    speed = distance / time  # Basic speed calculation (in m/s)
    return speed

# Function for occupancy detection
def detect_occupants(image_path):
    """
    Detects occupants from an image.
    
    Args:
        image_path (str): Path to the image file.
        
    Returns:
        Occupant detection result
    """
    occupancy_model = model_loader.get_model('occupancy_detection')
    img = image.load_img(image_path, target_size=(224, 224))  # Adjust size as per your model
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = occupancy_model.predict(img_array)
    return "Occupants detected"

# Example usage
if __name__ == "__main__":
    # Load and use models
    try:
        helmet_result = detect_helmet("path_to_video_file")  # Provide your actual video file path
        print(helmet_result)
        
        number_plate_result = recognize_number_plate("path_to_image_file")  # Provide your actual image file path
        print(number_plate_result)
        
        speed_result = calculate_speed(distance=100, time=10)
        print(f"Calculated speed: {speed_result} m/s")
        
        occupancy_result = detect_occupants("path_to_image_file")  # Provide your actual image file path
        print(occupancy_result)
    except KeyError as e:
        print(e)
