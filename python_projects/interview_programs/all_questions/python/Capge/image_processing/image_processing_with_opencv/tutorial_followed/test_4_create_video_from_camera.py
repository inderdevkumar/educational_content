
# Objective:
# Open camera, get frames and change the colour of frame. Show only red colour in camera

import cv2

all_colors_in_cv2= [item for item in dir(cv2) if item.startswith("COLOR_")]
print("all_colors_in_cv2: ", len(all_colors_in_cv2))

# vid= cv2.VideoCapture("path of video")  # If u like to load vide
load_camera= cv2.VideoCapture(0)

fourcc= cv2.VideoWriter_fourcc(*"XVID")
vid= cv2.VideoWriter(r"..\images_for_test\video1.avi", fourcc, 6, (640, 480))  # 6-> frame/sec, (640, 480)-> w,h of video

# Infinite number of frame can be captured like this
while True:
    tf, frame = load_camera.read()  # load_camera.read() Retruns (true/false, frame, dtype= uint8)
    # print(tf)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Converting to HSV is best way to filter colour

    vid.write(frame)
    cv2.imshow("Single Frame", frame) # It will just take one frame and show
    key= cv2.waitKey(1)  # For video

    # This is imp to break while
    if key == 27: # press esc key
        break

# Below are imp, as cam will be busy by zombie process and hence will create error while loading camera
load_camera.release()
vid.release()
cv2.destroyAllWindows()

