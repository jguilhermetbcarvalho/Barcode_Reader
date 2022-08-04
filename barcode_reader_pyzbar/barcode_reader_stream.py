# IMPORTS
import cv2
from pyzbar.pyzbar import decode
import time
from barcode_reader import BarcodeReader

# Class Barcode Reader
barcode = BarcodeReader()

# Select region of interest (ROI)
camera = cv2.VideoCapture(0)
ret, frame = camera.read()
# bbox = cv2.selectROI(frame, False)
# (w1, h1, w2, h2) = bbox
w1, h1, w2, h2 = 200, 220, 200, 100 # After select roi, determine points
# print(bbox)

# Streaming
while ret:
    # Capture of camera
    ret, frame = camera.read()
    
    # Flip in the frame
    frame = cv2.flip(frame,1)
    
    # ROI slice in the frame and resize
    roi = frame[h1:h1 + h2, w1:w1 + w2]
    roi = cv2.resize(roi, None, None, fx=1.8, fy=1.8)
    
    # Detect barcode
    barcodes = decode(roi)

    # ROI in the frame original
    cv2.rectangle(frame, (w1, h1), (w1+w2, h1+h2), (0, 0, 255), 2)

    # If detected barcode in the ROI
    if barcodes:
        time.sleep(2)
        cv2.rectangle(frame, (w1, h1), (w1+w2, h1+h2), (0, 255, 0), 2)
        frame = barcode.barcorde_stream(roi)

    cv2.imshow('Barcode/QR code reader', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    
# Close the windows
camera.release()
cv2.destroyAllWindows()
