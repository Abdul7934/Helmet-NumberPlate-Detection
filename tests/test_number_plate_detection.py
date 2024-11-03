import unittest
from app.modules.number_plate_detection import detect_number_plate

class TestNumberPlateDetection(unittest.TestCase):
    def test_detect_number_plate(self):
        image = "dummy_image"  # Replace with actual image or mock
        plate_number = detect_number_plate(image)
        self.assertIsNotNone(plate_number, "Number plate detection failed.")

if __name__ == "__main__":
    unittest.main()
