import cv2

image = cv2.imread("E:\\Learnings_and_Projects\GitHub-repo\\Learning_CV\\images\\profile.png")

if image is not None:
    cv2.putText(image, text="I am Ashish", org=(100, 100), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX, fontScale=2.0, color=(0,0,255), thickness=2, lineType=11)
    cv2.imshow("Text", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Not Loaded")