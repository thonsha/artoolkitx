import numpy as np
import cv2

if __name__ == '__main__':

    markerSet = ['M','I','F','L','Y','R']

    template = cv2.imread('cube-template-a4-2.png',0)
   

    cx = [827,  827,  1297, 827,  827,  357]
    cy = [1037, 567,  1037, 1977, 1507, 1037]

    i = 0
    for m in markerSet:
        
        marker = cv2.imread(m+'.jpg',0)
        marker2 = np.zeros([marker.shape[0]*2, marker.shape[1]*2],dtype=np.uint8)
        marker2.fill(255)
        marker2[128:128+256,128:128+256] = marker

        marker2 = cv2.resize(marker2, (470,470))
        template[cy[i]-235:cy[i]+235, cx[i]-235:cx[i]+235] = marker2
        
        i+=1

    name = ""
    for x in markerSet:
        name += x
    cv2.imwrite("template_"+ name +".jpg", template)
        