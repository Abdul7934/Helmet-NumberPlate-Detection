import unittest
from app.modules.alerts_notifications import send_alert

class TestAlertsNotifications(unittest.TestCase):
    def test_send_alert(self):
        message = "Test alert message"
        response = send_alert(message)
        self.assertTrue(response, "Failed to send alert.")

if __name__ == "__main__":
    unittest.main()
