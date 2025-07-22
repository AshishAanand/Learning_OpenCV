import cv2

image = cv2.imread("E:\\Learnings_and_Projects\\GitHub-repo\\Learning_CV\\images\\Saske.jpg")

if image is not None:

    cv2.imshow("Before", image)

    changed = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    cv2.imshow("After", changed)

    cv2.imwrite("E:\\Learnings_and_Projects\GitHub-repo\\Learning_CV\\edited\\Sasuke_Uchiha_new.jpg", changed)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image is not loaded succssfully BC")