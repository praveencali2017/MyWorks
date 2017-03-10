import cv2
import numpy as np
from cv2 import waitKey
import HSVFinder as finder
# np.set_printoptions(threshold=np.inf)
capture = cv2.VideoCapture(0)
while(1):
    ret_val, img=capture.read()
    cv2.imshow("original",img)
    cloned=img.copy()
    hsv = cv2.cvtColor(cloned, cv2.COLOR_BGR2HSV)
    # finder.constructTracbarsForHSV(hsv)
    # mask=cv2.inRange(hsv,finder.lowerboundHSV,finder.upperboundHSV)
    mask = cv2.inRange(hsv, np.array([92, 113, 109]), np.array([179, 255, 255]))
    kernel = np.ones((8, 8), np.uint8)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    image, contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        cv2.drawContours(cloned,[approx],-1,(0,255,0),3)
        x,y,h,w=cv2.boundingRect(c)
        # cv2.putText(cloned,"pen",(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
        # output = cv2.bitwise_and(img, img, mask = mask)
    cv2.imshow("detector",cloned)
    if waitKey(15)==27:
       cv2.destroyAllWindows()
       break;