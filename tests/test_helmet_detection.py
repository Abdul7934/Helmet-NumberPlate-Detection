import unittest
from app.modules.helmet_detection import detect_helmet

class TestHelmetDetection(unittest.TestCase):
    def test_detect_helmet(self):
        frame = "dummy_frame"  # Replace with actual frame or mock
        result = detect_helmet(frame)
        self.assertTrue(result, "Helmet detection failed.")

if __name__ == "__main__":
    unittest.main()
