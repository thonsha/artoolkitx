import numpy as np
import cv2
import random

meas=[]
pred=[]
canvas = np.zeros((128,128), np.uint8) # drawing canvas
drawing = False # true if mouse is pressed


def imgDiff(img1, img2):
    diff = img1 - img2
    err = np.sum(diff)

    return err

def onmouse(event,x,y,flags,params):
    global drawing, canvas
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        canvas[y//16*16:(y//16+1)*16, x//16*16:(x//16+1)*16] = 255
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            canvas[y//16*16:(y//16+1)*16, x//16*16:(x//16+1)*16] = 255

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

def clear():
    global canvas

    canvas = np.zeros((128,128), np.uint8)


if __name__ == '__main__':

    cv2.namedWindow("drawPattern")
    cv2.setMouseCallback("drawPattern",onmouse)

    while True:

        cv2.imshow("drawPattern",canvas)
        k = cv2.waitKey(30) &0xFF
        if k == 27 or k == 81 or k == 113: break
        if k == 67 or k == 99: clear()
        if k == 82 or k == 114:
            clear()
            for i in range(0,128,16):
                for j in range(0,128,16):
                    if random.random() < 0.5:
                        canvas[j:j+16, i:i+16] = 255
        if k == 32 : 
            img2 = np.rot90(canvas)
            err1 = imgDiff(canvas, img2)
            img3 = np.rot90(img2)
            err2 = imgDiff(canvas, img3)

            if err1 != 0 and err2 != 0:
                print("Rotationally asymmetric check passed. Saving file...")
                filename = input('filename: ')
                img = np.zeros((256,256), np.uint8)
                img[64:192, 64:192] = canvas
                
                cv2.imwrite(filename, img)
                clear()


            else:
                print("Rotationally asymmetric check failed. Please redraw the pattern.")
                clear()
    
    

