import cv2

image = cv2.imread("E:\\Learnings_and_Projects\\GitHub-repo\\Learning_CV\\images\\Saske.jpg")

if image is not None:
    resized = cv2.resize(image, (500, 600))
    cv2.imshow("Resized", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not loaded")