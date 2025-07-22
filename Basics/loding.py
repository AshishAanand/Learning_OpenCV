import cv2

# Loding Image

image = cv2.imread("Learning_CV/images/Saske.jpg")

if image is None:
    print("Image is not loaded successfully")
else:
    print("Image loaded successfully")