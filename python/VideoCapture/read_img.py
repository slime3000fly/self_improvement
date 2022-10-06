# program to capture video and change face to some image
#By: slime3000fly

import cv2 as cv


cap = cv.VideoCapture(0)

face = cv.CascadeClassifier(
    cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')


while True:
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_casade = face.detectMultiScale(gray, 1.2, 5)

    # Image.open('love.webp').convert('CMYK').save('result.jpg')

    face_img = cv.imread('love.jpg')

    for x, y, w, h in face_casade:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 5, 50), 10)
        face_img = cv.resize(face_img, (w, h))
        frame[y:y+face_img.shape[0], x:x+face_img.shape[1]] = face_img

    cv.imshow('camera', frame)

    if cv.waitKey(1) == ord('a'):
        break

cap.release()
cv.destroyAllWindows()
