import cv2

image = cv2.imread("E:\\Learnings_and_Projects\GitHub-repo\\Learning_CV\\images\\profile.png")


if image is not None:

    pt1 = (50, 100)
    pt2 = (400, 500)
    color = (125, 34, 120)

    cv2.rectangle(image, pt1=pt1, pt2=pt2, color=color, thickness=20)
    cv2.imshow("Rectangle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Not Loaded")