import cv2

image = cv2.imread("E:\\Learnings_and_Projects\\GitHub-repo\\Learning_CV\\images\\Saske.jpg", flags=0) # works well with grayscale images

resized_img = cv2.resize(image, (300, 300))

edges = cv2.Canny(image, 70, 150) # 0 -> 255
resized_edge = cv2.resize(edges, (300,300))

cv2.imshow("Original", resized_img)
cv2.imshow("edge", resized_edge)
cv2.waitKey(0)
cv2.destroyAllWindows()