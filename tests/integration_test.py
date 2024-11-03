import unittest
from app.modules.helmet_detection import detect_helmet
from app.modules.number_plate_detection import detect_number_plate
from app.modules.speed_detection import calculate_speed

class TestIntegration(unittest.TestCase):
    def test_integration(self):
        # Simulate integration of multiple modules
        frame = "dummy_frame"  # Replace with actual frame or mock
        image = "dummy_image"  # Replace with actual image or mock
        distance = 100  # meters
        time = 5  # seconds
        
        helmet_result = detect_helmet(frame)
        plate_number = detect_number_plate(image)
        speed = calculate_speed(distance, time)
        
        self.assertTrue(helmet_result, "Helmet detection integration failed.")
        self.assertIsNotNone(plate_number, "Number plate detection integration failed.")
        self.assertGreater(speed, 0, "Speed calculation integration failed.")

if __name__ == "__main__":
    unittest.main()
