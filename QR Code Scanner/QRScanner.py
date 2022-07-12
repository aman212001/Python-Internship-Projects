import cv2
import numpy as np
from pyzbar.pyzbar import decode                 #used for decoding the QRCODE


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
	success,img = cap.read()         #Reads Qrcode or Barcode
	for barcode in decode(img):
		#------------------------------------------Printing Data Part-------------------------------------------------------
		print(barcode.data)    #here data extracts the information stored in QR Code
		mydata = barcode.data.decode('utf-8')
		print(mydata)
		

		#------------------------------------------Generating Polygon on Barcode/QR Code part------------------------------
		pts = np.array([barcode.polygon],np.int32)
		pts = pts.reshape((-1,1,2))
		cv2.polylines(img,[pts],True,(255,0,255),5)      #Polylines on image with points generated and second last arg is colour and last arg is border 
		

		#---------------------------------------Displaying Text on Barcode/QrCode part------------------------------------
		pts2 = barcode.rect           #Barcodes axis points are extracted 
		cv2.putText(img,mydata,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)      #Data will be displayed on QR Code
		

	cv2.imshow('Result',img)
	cv2.waitKey(1)
	



