import unittest
from app.modules.speed_detection import calculate_speed

class TestSpeedDetection(unittest.TestCase):
    def test_calculate_speed(self):
        distance = 100  # meters
        time = 5  # seconds
        expected_speed = 72.0  # km/h
        speed = calculate_speed(distance, time)
        self.assertAlmostEqual(speed, expected_speed, places=1)

if __name__ == "__main__":
    unittest.main()
