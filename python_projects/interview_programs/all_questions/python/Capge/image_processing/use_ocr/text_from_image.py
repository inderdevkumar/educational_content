
# steps:
# import libary like opencv, pytesseract
# read the image from where we like to get text
# read the text from image

import PIL import Image
import pytesseract
from pytesseract  import Output
import cv2

my_config= r"--psm 6 --oem 3"

def method_1():
    # simple just read the text from image
    pillow_img= Image.open(r"test_images/3.jpg")
    text= pytesseract.image_to_string(pillow_img, config= my_config)
    print(text)


def method_2():
    # draw reactangle over the text found on the image
    cv_img= cv2.imread(r"test_images/3.jpg")

    # To draw reactangle boxes
    height, width, _ = cv_img.shape  # last variable is imp else throw error
    boxes= pytesseract.image_to_boxes(cv_img, config= my_config)
    #print(boxes)  # This will show cordinates of each individual characters eg: g 178 16 215 70 0

    for box in boxes.splitlines():
        box= box.split(" ")
        #print(box, height)
        cv_img= cv2.rectangle(cv_img, (int(box[1]), height- int(box[2])), (int(box[3]), height- int(box[4])),
                              (0, 255, 0), 2)  # 2 IS THICKNESS
    cv2.imshow("Image: ", cv_img)
    cv2.waitKey(0)


def method_3():
    cv_img= cv2.imread(r"test_images/3.jpg")
    # To draw reactangle boxes
    height, width, _ = cv_img.shape  # last variable is imp else throw error
    data= pytesseract.image_to_data(cv_img, config= my_config, output_type= Output.DICT)

    # print(data.keys())  # All keys
    print(data["text"])  # All text


    # And to tune it

    amount_boxes= len(data["text"])

    for i in range(amount_boxes):

        if (float(data["conf"][i]) > 60):
            (x, y, width, height)= (data["left"][i], data["top"][i], data["width"][i], data["height"][i])
            cv_img = cv2.rectangle(cv_img, (x, y), (x+width, y+height),
                                   (0, 255, 0), 2)
            print(data["text"][i])
            cv_img= cv2.putText(cv_img,data["text"][i], (x, y+height+15), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)  # Wroitw oon image
    cv2.imshow("Image: ", cv_img)
    cv2.waitKey(0)   # To give wait

method_3()