# IMPORTS
from pyzbar.pyzbar import decode, ZBarSymbol
from io import BytesIO
from PIL import Image
from base64 import b64decode
import cv2 as cv
import numpy as np

class BarcodeReader():
    
    def __init__(self) -> None:
        print("Barcode reader initialized.")

    # Barcode reader with Open CV and image base64
    def leitura_base64_OpenCV(image_base64): 

        # Decode image base64
        im_bytes = b64decode(image_base64)
        im_arr = np.frombuffer(im_bytes, dtype=np.uint8) 
        img = cv.imdecode(im_arr, flags=cv.IMREAD_COLOR)
        
        # Barcode reader
        detectedBarcodes = decode(img, symbols=[ZBarSymbol.EAN13, ZBarSymbol.EAN8]) 
        
        # Result
        if not detectedBarcodes: 
            return "Código de barra não encontrado!"
        else: 
            for barcode in detectedBarcodes: 
                if barcode.data!="":
                    return barcode.data.decode('utf-8')
    
    # Barcode reader with PILLOW and image base64        
    def leitura_base64_PIL(image_base64): 

        # Decode image base64
        img_bytes = b64decode(image_base64)
        img_file = BytesIO(img_bytes)
        img = Image.open(img_file)

        # Barcode reader
        detectedBarcodes = decode(img, symbols=[ZBarSymbol.EAN13, ZBarSymbol.EAN8]) 
        
        # Result
        if not detectedBarcodes: 
            return "Código de barra não encontrado!"
        else: 
            for barcode in detectedBarcodes: 
                if barcode.data!="":
                    return barcode.data.decode('utf-8')

    # Barcode reader with Open CV and image not base64
    def leitura_OpenCV(image): 

        # Capture image
        img = cv.imread(image)
        
        # Barcode reader
        detectedBarcodes = decode(img, symbols=[ZBarSymbol.EAN13, ZBarSymbol.EAN8]) 
        
        # Result
        if not detectedBarcodes: 
            return "Código de barra não encontrado!"
        else: 
            for barcode in detectedBarcodes: 
                if barcode.data!="":
                    return barcode.data.decode('utf-8')
                
    # Barcode read streaming
    def barcorde_stream(frame):
        
        # Detect barcorde
        barcodes = decode(frame)
        
        # If detected
        for barcode in barcodes:
            # Points rectangle barcode
            x, y , w, h = barcode.rect
            
            # reader result
            barcode_info = barcode.data.decode('utf-8')
            
            # Rectangle barcode and write barcode in the frame
            cv.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
            font = cv.FONT_HERSHEY_DUPLEX
            cv.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (0, 255, 100), 1)

            print(barcode_info)
        return frame
