import cv2
import numpy as np
from pyzbar.pyzbar import decode  # used for decoding the QRCODE

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

#---------------------------------------------Extracting data from a text file------------------------------------------
with open('myDataFile.text') as f:
    myDataList = f.read().splitlines()      #Every line is a new item


while True:
    success, img = cap.read()  # Reads Qrcode or Barcode
    for barcode in decode(img):
        # ------------------------------------------Printing Data Part--------------------------------------------------
        print(barcode.data)  # here data extracts the information stored in QR Code
        mydata = barcode.data.decode('utf-8')
        print(mydata)


        if mydata in myDataList:
            myOutput = 'Authorized'
            mycolour = (0,255,0)
        else:
            myOutput = 'Un-Authorized'
            mycolour = (0,0,255)

        # ------------------------------------------Generating Polygon on Barcode/QR Code part--------------------------
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True,mycolour ,
                      5)  # Polylines on image with points generated and second last arg is colour and last arg is border

        # ---------------------------------------Displaying Text on Barcode/QrCode part---------------------------------
        pts2 = barcode.rect  # Barcodes axis points are extracted
        cv2.putText(img, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, mycolour,
                    2)  # Data will be displayed on QR Code

    cv2.imshow('Result', img)
    cv2.waitKey(1)
    