import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(1)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    height, width, channels = frame.shape
else:
    rval = False
    print('no webcam detected')

while rval:
    cv2.imshow("webcam", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27:  #exit key on ESC#
        break

cv2.destroyWindow("webcam")