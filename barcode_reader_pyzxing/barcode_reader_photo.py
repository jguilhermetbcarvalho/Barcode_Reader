# IMPORT'S
from pyzxing import BarCodeReader
import cv2 as cv

# PATH IMAGE
path = 'barcode/barcorde_0.png'

# BARCODE READER
reader = BarCodeReader()
detectedBarcodes = reader.decode(path)

# PRINT OF RESULT
for barcode in detectedBarcodes:
    if barcode['raw']:
        print(barcode['raw'].decode('utf8'))
        