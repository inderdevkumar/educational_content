# link to follow: https://github.com/ibrahimokdadov/openCV3_tutorials

import cv2
img= cv2.imread(r"..\images_for_test\laptop.jpg")
# print(img)  to print image in numpy array

if img is None:
    print("Object does nkot exist")

else:
    cv2.imshow("laptop_image", img)  # To give a title to the image when shown
    cv2.waitKey(0)  # Just to view the image, else it will disapper very fast
    # cv2.destroyAllWindows()


