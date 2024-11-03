import cv2
import pytesseract

def detect_number_plate(frame):
    # Preprocess the image for better OCR results
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    
    # Use pytesseract to extract text
    config = r'--oem 3 --psm 6'
    number_plate = pytesseract.image_to_string(thresh, config=config)

    return number_plate.strip()  # Returns the recognized number plate
