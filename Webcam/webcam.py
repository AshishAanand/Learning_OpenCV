import cv2


cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    if not ret:
        print("Not Working")
        break

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        print("Closing")
        break

cam.release() 
cv2.destroyAllWindows()

    