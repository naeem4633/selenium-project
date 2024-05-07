import cv2
import numpy as np

def detect_screen_color(screen_path):
    # Load screenshot
    screenshot = cv2.imread(screen_path)

    # Define region of interest (ROI) as a percentage of the screen size
    height, width, _ = screenshot.shape
    roi_start_x = int(width * 0.3)
    roi_start_y = int(height * 0.3)
    roi_end_x = int(width * 0.9)
    roi_end_y = int(height * 0.9)

    # Crop ROI from screenshot
    roi = screenshot[roi_start_y:roi_end_y, roi_start_x:roi_end_x]

    # Convert ROI to grayscale
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, binary_roi = cv2.threshold(gray_roi, 50, 255, cv2.THRESH_BINARY)

    # Calculate percentage of black and white pixels
    total_pixels = binary_roi.size
    black_pixels = np.count_nonzero(binary_roi == 0)
    white_pixels = np.count_nonzero(binary_roi == 255)
    black_pixel_percentage = (black_pixels / total_pixels) * 100
    white_pixel_percentage = (white_pixels / total_pixels) * 100

    # Define thresholds for considering the screen as black or white
    black_threshold = 90
    white_threshold = 90

    # Check if black or white pixel percentage exceeds thresholds
    if black_pixel_percentage > black_threshold:
        return "black"
    elif white_pixel_percentage > white_threshold:
        return "white"
    else:
        return "none"
    
def black_screen_detected(screen_path):
    return detect_screen_color(screen_path) == "black"

def white_screen_detected(screen_path):
    return detect_screen_color(screen_path) == "white"

def detect_screen_color_small_area(screen_path):
    # Load screenshot
    screenshot = cv2.imread(screen_path)

    # Define region of interest (ROI) as a percentage of the screen size
    height, width, _ = screenshot.shape
    roi_start_x = int(width * 0.4)
    roi_start_y = int(height * 0.4)
    roi_end_x = int(width * 0.6)
    roi_end_y = int(height * 0.6)

    # Crop ROI from screenshot
    roi = screenshot[roi_start_y:roi_end_y, roi_start_x:roi_end_x]

    # Convert ROI to grayscale
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, binary_roi = cv2.threshold(gray_roi, 50, 255, cv2.THRESH_BINARY)

    # Calculate percentage of black and white pixels
    total_pixels = binary_roi.size
    black_pixels = np.count_nonzero(binary_roi == 0)
    white_pixels = np.count_nonzero(binary_roi == 255)
    black_pixel_percentage = (black_pixels / total_pixels) * 100
    white_pixel_percentage = (white_pixels / total_pixels) * 100

    # Define thresholds for considering the screen as black or white
    black_threshold = 90
    white_threshold = 90

    # Check if black or white pixel percentage exceeds thresholds
    if black_pixel_percentage > black_threshold:
        return "black"
    elif white_pixel_percentage > white_threshold:
        return "white"
    else:
        return "none"
    
def black_screen_detected_small_area(screen_path):
    return detect_screen_color_small_area(screen_path) == "black"
    
# Example usage:
# screen_path = "./image.png"
# result = black_screen_detected_small_area(screen_path)
# print(result)
