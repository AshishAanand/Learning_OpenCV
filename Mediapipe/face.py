import cv2
import mediapipe as mp

cam = cv2.VideoCapture(0)

# Face mesh detection setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)
mp_draw = mp.solutions.drawing_utils

while True:
    success, img = cam.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(img_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_draw.draw_landmarks(img, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION)

    cv2.imshow("Face Mesh Tracking", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
