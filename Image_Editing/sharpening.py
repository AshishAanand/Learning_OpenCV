import cv2
import numpy as np

image = cv2.imread("E:\\Learnings_and_Projects\\GitHub-repo\\Learning_CV\\images\\Saske.jpg")

if image is not None:

    kernal = np.array([
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ])

    sharped = cv2.filter2D(image, -1, kernal)

    cv2.imshow("Original", image)
    cv2.imshow("Sharped", sharped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Not Loaded")