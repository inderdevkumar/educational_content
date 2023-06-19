

"""
link to follow: https://pythonexamples.org/python-opencv/
"""

import cv2
import numpy as np

class reading_image:
    def Read_color_image_using_imread(self):
        """
        The syntax of cv2.imread() function is given below: cv2.imread(/path/to/image, flag). And below 3 can be used as flag
        cv2.IMREAD_COLOR reads the image with RGB colors but no transparency channel.
        cv2.IMREAD_GRAYSCALE reads the image as grey image.
        cv2.IMREAD_UNCHANGED reads the image as is from the source.
        """
        # read image
        img = cv2.imread(r'../test_images/2.jpg')
        # print its shape
        print('Image Dimensions :', img.shape)  # Image Dimensions : (180, 466, 3)
        print(f"Height of image: {img.shape[0]}pixel, width is: {img.shape[1]} pixel and colour channel is: {img.shape[2]}")

    def Read_image_as_greyscale(self):
        img = cv2.imread(r'../test_images/2.jpg', cv2.IMREAD_GRAYSCALE)
        print('Image Dimensions :', img.shape)  # Image Dimensions : (180, 466)
        print(f"Height of image: {img.shape[0]}pixel, width is: {img.shape[1]} pixel")

    def Read_image_as_transparency_channel(self):
        # We have read all the four channels of the image. Namely Red, Green, Blue and Transparency.
        img = cv2.imread(r'../test_images/2.jpg', cv2.IMREAD_UNCHANGED)
        print('Image Dimensions :', img.shape)  # Image Dimensions : (180, 466, 4)
        print(f"Height of image: {img.shape[0]}pixel, width is: {img.shape[1]} pixel and colour channel is: {img.shape[2]}")

# read= reading_image()
# read.Read_color_image_using_imread()
# read.Read_image_as_greyscale()
# read.Read_image_as_transparency_channel()

class save_image:
    def save_using_imwrite(self):
        # The syntax of imwrite() function is: cv2.imwrite(path, image)
        # cv2.imwrite() returns a boolean value.
        # read image as grey scale
        img = cv2.imread(r'../test_images/2.jpg')
        # do some transformations on img

        # save matrix/array as image file
        isWritten = cv2.imwrite(r'../test_images/write2.jpg', img)

        if isWritten:
            print('Image is successfully saved as file.')


    def Save_image_created_with_random_pixel(self):
        img = np.random.randint(255, size=(300, 600, 3))
        isWritten = cv2.imwrite(r'../test_images/write2.jpg', img)


# write= save_image()
# write.save_using_imwrite()
# write.Save_image_created_with_random_pixel()

class Resize_Image:

    def use_resize(self):
        # Following is the syntax of cv2.resize() function.
        # cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) where
        # src is the source, original or input image in the form of numpy array
        # dsize is the desired size of the output image, given as tuple
        # fx is the scaling factor along X-axis or Horizontal axis
        # fy is the scaling factor along Y-axis or Vertical axis
        # interpolation could be one of the following values (INTER_NEAREST, INTER_LINEAR, INTER_AREA, INTER_CUBIC, INTER_LANCZOS4)

        src = cv2.imread(r"../test_images/2.jpg", cv2.IMREAD_UNCHANGED)

        # percent by which the image is resized
        scale_percent = 50

        # calculate the 50 percent of original dimensions
        width = int(src.shape[1] * scale_percent / 100)
        height = int(src.shape[0] * scale_percent / 100)

        # dsize
        dsize = (width, height)

        # resize image
        output = cv2.resize(src, dsize)

        cv2.imwrite(r'../test_images/write3.jpg', output)

    def  Resize_image_only_horizontally(self):
        src = cv2.imread(r"../test_images/2.jpg", cv2.IMREAD_UNCHANGED)

        # calculate the 50 percent of original dimensions
        new_width = int(src.shape[1])+ 50
        height= src.shape[0]
        dsize = (new_width, height)

        output = cv2.resize(src, dsize, interpolation = cv2.INTER_AREA)

        cv2.imwrite(r'../test_images/resize_4.jpg', output)

    def convert_coloured_image_to_binary_image(self):
        # Read the source image as grey scale image.
        # Convert the grey scale image to binary with a threshold of your choice.
        pass

    def Convert_color_image_to_black_n_white(self):
        # read image
        img_grey = cv2.imread(r"../test_images/2.jpg", cv2.IMREAD_GRAYSCALE)
        colour_img = cv2.imread(r"../test_images/2.jpg")
        # define a threshold, 128 is the middle of black and white in grey scale
        thresh = 128
        # threshold the image
        img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]
        img_binary_colour = cv2.threshold(colour_img, thresh, 100, cv2.THRESH_BINARY)[1]
        # save image
        cv2.imwrite(r'../test_images/grey_5.jpg', img_grey)
        cv2.imwrite(r'../test_images/black_n_white_6.jpg', img_binary)
        cv2.imwrite(r'../test_images/black_n_white_7_from_colour.jpg', img_binary_colour)


# resize= Resize_Image()
# resize.use_resize()
# resize.Resize_image_only_horizontally()
# resize.Convert_color_image_to_black_n_white()

class Image_Operations:

    def write_text_on_image_using_putText(self):

        # we write text on the image from the position (10, 50) i.e., 10 pixels from the top, and 50 pixels from the left.
        image = cv2.imread(r"../test_images/2.jpg", cv2.IMREAD_UNCHANGED)

        position = (10, 95)
        cv2.putText(
            image,  # numpy array on which text is written
            "writing TEXT!",  # text
            position,  # position at which writing has to start
            cv2.FONT_HERSHEY_SIMPLEX,  # font family
            1,  # font size
            (209, 80, 0, 255),  # font color
            2)  # font stroke
        cv2.imwrite(r'../test_images/write_text_8.jpg', image)

    def Write_text_at_the_center_of_the_image(self):
        image = cv2.imread(r"../test_images/2.jpg", cv2.IMREAD_UNCHANGED)
        # print(image.shape)
        position = ((int(image.shape[1])//2)-int(image.shape[1])//4, int(image.shape[0])//2)  # (width, height)
        cv2.putText(
            image,  # numpy array on which text is written
            "writing TEXT!",  # text
            position,  # position at which writing has to start
            cv2.FONT_HERSHEY_SIMPLEX,  # font family
            1,  # font size
            (209, 80, 0, 255),  # font color
            2)  # font stroke
        cv2.imwrite(r'../test_images/write_text_9_center.jpg', image)

    def Add_or_Blend_Two_Images(self):
        # you can add or blend two images with the help of cv2.addWeighted() method.
        # syntax of addWeighted() function.: dst = cv.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]])
        # read two images, and they should have simmilar shape
        src1 = cv2.imread(r"../test_images/2.jpg", cv2.IMREAD_COLOR)
        src2 = cv2.imread(r"../test_images/2.jpg", cv2.IMREAD_COLOR)
        # add or blend the images
        dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
        # save the output image
        cv2.imwrite(r"../test_images/10_add_blend.jpg", dst)

    def find_contours_in_an_image(self):
        # To find contours in an image, follow these steps:
        # Read image as grey scale image.
        # Use cv2.threshold() function to obtain the threshold image.
        # Use cv2.findContours() and pass the threshold image and necessary parameters.
        # findContours() returns contours. You can draw it on the original image or a blank image.

        img = cv2.imread(r"../test_images/2.jpg", cv2.IMREAD_UNCHANGED)

        # convert img to grey
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # set a thresh
        thresh = 100
        # get threshold image
        ret, thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
        # find contours
        contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # create an empty image for contours
        img_contours = np.zeros(img.shape)
        # draw the contours on the empty image
        cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 3)
        # save image
        cv2.imwrite(r"../test_images/11_contour.jpg", img_contours)

# operation= Image_Operations()
# operation.write_text_on_image_using_putText()
# operation.Write_text_at_the_center_of_the_image()
# operation.Add_or_Blend_Two_Images()
# operation.find_contours_in_an_image()

class colour_channels:

    def extract_Red_Channel_of_Color_Image(self):
        # steps to extract red channel from an image.
        # Read image using cv2.imread().
        # imread() returns BGR (Blue-Green-Red) array. It is three dimensional array i.e., 2D pixel arrays for three color channels.
        # Extract the red channel alone by slicing the array.

        # read image
        src = cv2.imread(r"../test_images/7.jpg", cv2.IMREAD_UNCHANGED)
        #print(src.shape)

        # extract red channel
        red_channel = src[:, :, 2]  # (Blue-Green-Red)
        #print(red_channel)

        # create empty image with same shape as that of src image
        red_img = np.zeros(src.shape)

        # assign the red channel of src to empty image
        red_img[:, :, 2] = red_channel

        # write red channel to greyscale image
        cv2.imwrite(r"../test_images/12_extract_red.jpg", red_img)

    def extract_green_Channel_of_Color_Image(self):
        # read image
        src = cv2.imread(r"../test_images/7.jpg", cv2.IMREAD_UNCHANGED)
        #print(src.shape)

        # extract red channel
        green_channel = src[:, :, 1] # (Blue-Green-Red)
        #print(red_channel)

        # create empty image with same shape as that of src image
        green_img = np.zeros(src.shape)

        # assign the red channel of src to empty image
        green_img[:, :, 1] = green_channel

        # write red channel to greyscale image
        cv2.imwrite(r"../test_images/13_extract_green.jpg", green_img)

# colour= colour_channels()
# colour.extract_Red_Channel_of_Color_Image()
# colour.extract_green_Channel_of_Color_Image()

class Video_with_OpenCV:

    def Capture_Video(self):
        # capture frames from a camera with device index=0
        cap = cv2.VideoCapture(0)  #primary camera

        # loop runs if capturing has been initialized
        while (1):

            # reads frame from a camera
            ret, frame = cap.read()  # cap.read() Retruns (true/false, frame, dtype= uint8)

            # Display the frame
            cv2.imshow('Camera', frame)

            # Wait for 25ms
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # release the camera from video capture
        cap.release()

        # De-allocate any associated memory usage
        cv2.destroyAllWindows()

video= Video_with_OpenCV()
video.Capture_Video()