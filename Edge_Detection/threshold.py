import cv2

img = cv2.imread("E:\\Learnings_and_Projects\\GitHub-repo\\Learning_CV\\images\\Saske.jpg")

resized_img = cv2.resize(img, (500, 500))

ret, thres_img = cv2.threshold(img, 90, 255, cv2.THRESH_BINARY)

resized_thresh = cv2.resize(thres_img, (500, 500))

cv2.imwrite("E:\\Learnings_and_Projects\\GitHub-repo\\Learning_CV\\edited\\Threshold_Sasuke_image.jpg", thres_img)
print("Saved")

cv2.imshow("original", resized_img)
cv2.imshow("threshold", resized_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()