#created by ElectroBoY    @dhanushkasct1947 github

#import lib
import cv2
from pyzbar import pyzbar
#open image
img = cv2.imread("images/img1.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #converto gryscale
#start decode
barcodes = pyzbar.decode(gray)
for barcode in barcodes : 
    x,y,w,h = barcode.rect
    barData= barcode.data.decode("utf-8")
    barType = barcode.type
    print(x,y,w,h)  #barcode rec values
    print(barData,barType)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,205,0),16,8)
    cv2.rectangle(img,(x+100,y-400),(x+1300,y-200),(255,255,255),200,8)
    cv2.putText(img,barData,(x+70,y-250),cv2.FONT_HERSHEY_PLAIN,10,(0,0,255),10,30)


cv2.imshow("Original Image with BarCode",img)
cv2.waitKey(0)
cv2.destroyAllWindows()