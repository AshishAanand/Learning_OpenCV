import cv2

image = cv2.imread("E:\\Learnings_and_Projects\GitHub-repo\\Learning_CV\\images\\profile.png")


if image is not None:

    center = (500, 500)
    color = (0,0,0)

    cv2.circle(image, center=center, radius=100, color=color, thickness=10)
    cv2.imshow("Circle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Not Loaded")