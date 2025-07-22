import cv2

image = cv2.imread("E:\\Learnings_and_Projects\\GitHub-repo\\Learning_CV\\images\\Saske.jpg")

(h, w) = image.shape[:2]

center = (h//2, w//2)

if image is not None:
    rotation_matrix = cv2.getRotationMatrix2D(center=center, angle=15, scale=1)
    rotated_img = cv2.warpAffine(image, rotation_matrix, (h, w))

    cv2.imshow("Rotated image", rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Not loaded")