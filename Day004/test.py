import cv2
import time
import numpy as np


img_path = './Part01/lena.png'
img = cv2.imread(img_path)

while True:
    '''
    cv2.startWindowThread()
    cv2.namedWindow("change saturation")
    '''
    cv2.imshow('change saturation', img)
    
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        '''
        cv2.waitKey(1)
        
        cv2.waitKey(1)
        cv2.waitKey(1)
        cv2.waitKey(1)
        '''
        break