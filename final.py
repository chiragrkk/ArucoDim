import cv2
import numpy as np
from object_detector import HomogeneousBgDetector

# Marker size in cm (change as per your printed marker size)
MARKER_SIZE_CM = 5  

# ArUco setup (OpenCV 4.7+ syntax)
parameters = cv2.aruco.DetectorParameters()
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_50)
detector_aruco = cv2.aruco.ArucoDetector(aruco_dict, parameters)

# Object detector
detector = HomogeneousBgDetector()

# Load image (replace with your file path)
img_path = "test_image.jpg"
img = cv2.imread(img_path)

if img is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Detect ArUco markers
corners, ids, _ = detector_aruco.detectMarkers(img)

if len(corners) > 0:
    int_corners = corners[0].astype(int)
    cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

    aruco_perimeter = cv2.arcLength(corners[0], True)
    pixel_cm_ratio = aruco_perimeter / (MARKER_SIZE_CM * 4)

    contours = detector.detect_objects(img)

    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        (x, y), (w, h), angle = rect

        if w == 0 or h == 0:
            continue

        object_width = w / pixel_cm_ratio
        object_height = h / pixel_cm_ratio

        box = cv2.boxPoints(rect).astype(int)
        cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
        cv2.polylines(img, [box], True, (255, 0, 0), 2)

        cv2.putText(img, f"Width: {round(object_width, 1)} cm",
                    (int(x - 100), int(y - 20)),
                    cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
        cv2.putText(img, f"Height: {round(object_height, 1)} cm",
                    (int(x - 100), int(y + 15)),
                    cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)

# Show result
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
