import cv2
from time import sleep, time


if __name__ == "__main__":
    delay = 10
    timeout = 5
    print(timeout)
    start_time = time()
    face_cascade_path = "haarcascade/haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    faces = []
    cap = cv2.VideoCapture(0)
    while time() - start_time <= timeout:
        ret, img = cap.read()
        img = cv2.imread("./dummy.png")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        print(faces)
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = img[y: y + h, x: x + w]
            face_gray = gray[y: y + h, x: x + w]
        cv2.imshow("image", img)
        key = cv2.waitKey(delay)
    print(time() - start_time)
        # sleep(1)
        
        