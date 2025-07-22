import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc('XVID') # this line is creating issue

recorded = cv2.VideoWriter("recorded.mp4", codec, 20, (frame_width, frame_height))

while True:
    scu, img = camera.read()

    recorded.write(img)
    cv2.imshow("recording", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()