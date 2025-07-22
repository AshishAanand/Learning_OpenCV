import cv2

image = cv2.imread("E:\\Learnings_and_Projects\\GitHub-repo\\Learning_CV\\images\\profile.png")

if image is not None:
    resized = cv2.resize(image, (500, 500))
    flipped_img = cv2.flip(resized, flipCode=1) # Passing 1 -> Flib Horizontally, 0 -> Flip Vertivally, -1 -> Filp both direction
    cv2.imshow("Original", image)
    cv2.imshow("Profile image",flipped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Not Loaded")