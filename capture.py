import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    resultimage = cv.GaussianBlur(gray, (7, 7), 0)
    ret,thresh = cv.threshold(resultimage,127,255,cv.THRESH_BINARY)
    edged = cv.Canny(resultimage, 20, 200)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #cv.drawContours(thresh, contours, 0, (0,255,0), 3)
    # Display the resulting frame
    cv.drawContours(frame, contours, -1, (0, 255, 0), 3)

    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        print("Number of Contours found = " + str(len(contours)))
        cv.imwrite("/Users/edwardhaynes/Documents/PYTHON-PROJECT/capture.png", frame)
        break

    # counting the number of pixels
    number_of_white_pix = np.sum(thresh == 255)
    number_of_black_pix = np.sum(thresh == 0)
    perimeter1 = cv.arcLength(contours[0],True)
    perimeter2 = cv.arcLength(contours[1],True)


    print('Number of white pixels:', number_of_white_pix)
    print('Number of black pixels:', number_of_black_pix)
    print('Perimeter1 length:', perimeter1)
    print('Perimeter2 length:', perimeter2)
    #print('Contour area:', area)


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()