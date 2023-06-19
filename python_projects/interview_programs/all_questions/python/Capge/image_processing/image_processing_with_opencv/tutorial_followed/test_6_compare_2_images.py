# Its very powerful to compare two images, whether its plain image or text written image




import cv2
import numpy as np

img1= cv2.imread(r"..\images_for_test\text_on_image1.jpg")
img2= cv2.imread(r"..\images_for_test\text_on_image1_b.jpg")

diff= cv2.subtract(img1, img2)
result= not np.any(diff)  #If diff is all 0, it will return false

if result is True:
    print("images are same")
else:
    cv2.imwrite(r"..\images_for_test\diff.jpg", diff)
    print("Image is diff")