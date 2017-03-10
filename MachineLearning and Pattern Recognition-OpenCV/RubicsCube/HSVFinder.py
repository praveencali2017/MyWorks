import  numpy as np
import cv2
imgHeight=0
imgWidth=0
h,s,v = 0,0,0
img = np.zeros((300,512,3), np.uint8)
# cv2.namedWindow('hsv')
lowerboundHSV = np.array([h, s, v])
upperboundHSV = np.array([179, 255, 255])
def callBackForTrackbars(x):
    h = cv2.getTrackbarPos('h', 'hsv')
    s = cv2.getTrackbarPos('s', 'hsv')
    v = cv2.getTrackbarPos('v', 'hsv')
    lowerboundHSV = np.array([h, s, v])
    mask = cv2.inRange(hsvImage,lowerboundHSV, upperboundHSV)
    # cv2.imshow("hsv",mask)
def constructTracbarsForHSV(image):
    h, w = image.shape[:2]
    global hsvImage
    hsvImage=np.ndarray(shape=(h,w))
    hsvImage=image
    cv2.createTrackbar('h', 'hsv', 0, 179, callBackForTrackbars)
    cv2.createTrackbar('s', 'hsv', 0, 255, callBackForTrackbars)
    cv2.createTrackbar('v', 'hsv', 0, 255, callBackForTrackbars)
    mask = cv2.inRange(hsvImage, lowerboundHSV, upperboundHSV)
    # cv2.imshow("hsv", mask)
