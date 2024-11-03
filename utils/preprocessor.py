import cv2

class VideoPreprocessor:
    def __init__(self, target_width=640, target_height=480):
        self.target_width = target_width
        self.target_height = target_height

    def preprocess_frame(self, frame):
        # Resize the frame to the target dimensions
        resized_frame = cv2.resize(frame, (self.target_width, self.target_height))
        # Convert to grayscale for easier processing (if needed)
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        # Normalizing the image can also be done if needed
        normalized_frame = gray_frame / 255.0
        return normalized_frame

    def preprocess_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        processed_frames = []

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            processed_frame = self.preprocess_frame(frame)
            processed_frames.append(processed_frame)

        cap.release()
        return processed_frames
