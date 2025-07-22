import cv2

image = cv2.imread("E:\\Learnings_and_Projects\\GitHub-repo\\Learning_CV\\images\\banner.png")

if image is not None:
    cropped_text = image[240:370, 430:1000]
    crooped_lamp = image[100:300, 100:500]
    cv2.imshow("Original", image)
    cv2.imshow("Text", cropped_text)
    cv2.imshow("Lamp", crooped_lamp)

    # image_shape = image.shape
    # print(image_shape)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Not Loaded")