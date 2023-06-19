# photos of camers tsored in: C:\Users\HIMADRI TANAYA\AppData\Roaming\Microsoft\Windows\Libraries\CameraRoll.library-ms


import cv2

img= cv2.imread(r"..\images_for_test\inder3.jpg")
face_csc= cv2.CascadeClassifier("haar_cascade_face_detection.xml")
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces= face_csc.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 5)

cv2.imshow("image", img)
cv2.waitKey(0)