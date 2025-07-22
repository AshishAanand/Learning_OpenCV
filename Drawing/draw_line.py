import cv2

image = cv2.imread("E:\\Learnings_and_Projects\GitHub-repo\\Learning_CV\\images\\profile.png")

if image is not None:
    p1 = (50,100)
    p2 = (200,150)
    color = (0, 0, 255)
    thikness = 10

    cv2.line(image, p1, p2, color=color, thickness=thikness)

    cv2.imshow("Line", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Not Loaded")