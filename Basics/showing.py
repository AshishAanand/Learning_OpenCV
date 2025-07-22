import cv2

# Loding Image

image = cv2.imread("E:\\Learnings_and_Projects\\GitHub-repo\\Learning_CV\images\\Saske.jpg", flags=0) # in this line of code flags argument asks from you that in which color channel you want to load this image 0 -> Grayscale image and 1 -> RGB image

if image is not None:
    cv2.imshow("Saske Uchiha", image)

    cv2.waitKey(0) # Input is captured as miliseconds in this case 2000 == 2 seconds and 0 means whait for user to close it manually and if you input negative values then it will work similar as 0
    cv2.destroyAllWindows() # Colse option for user
else:
    print("Image is not loaded successfully")