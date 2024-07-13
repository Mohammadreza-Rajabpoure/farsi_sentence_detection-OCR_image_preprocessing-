'''
In this function we are going to crop each text lines from the image , input of function is a list of images
that each image cotaines one paragraph of the source image, and the output is a multipule dictionary that
containes images of each text lines of paragraphs

1st >> (line 29 to 34) >> import necessary libraries and modules

2nd >> (line 41) >> iterate each paragraph image with a for loop

3nd >> (line 43) >> use Threshold() function from src.threshold to detect all the text pixels

4nd >> (line 46) >> set a kernel with 3 hight and 30 wight to containe all the chararcters i a text line
such as dots,numbers,...

5nd >> (line 49) >> dilate the image width the kernel and iteration 1 pixel to connect all characters 
in text line 

6nd >> (line 52) >> set a contour for each dilated line width cv2.findContours

7nd >> (line 55) >> filter the contours for only contours widght biger than 20 pixels

8nd >> (line 58) >> sort the contours for only text lines using againe cv2.boungingRect

9nd >> (line 63 to 77) >> find the coordinate of each contour and crop that coordinate from image of paragraph
to detect the line and save it to a dictionary 
'''


import cv2
from text_detect.src.threshold import Threshold

def Line_detect(list_of_paragraphs):

    paragraphs={}
    parag = 0

    for image in list_of_paragraphs :

        all = Threshold(image)#find all texts by thresholding the image
        
        #set a rectangular kernel for each line
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 3))
        
        #connect all the words of each line
        dilation = cv2.dilate(all, rect_kernel, iterations = 1)
        
        #set a contour for each line
        contours, _ = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        #filter contours for only lines 
        filtered_contours = [cnt for cnt in contours if (cv2.boundingRect(cnt)[2] / cv2.boundingRect(cnt)[3])>=20.0]
        
        #sorting contours from top to bottom
        sorted_contours = sorted(filtered_contours, key=lambda contour: cv2.boundingRect(contour)[1])

        text_images = {}
        counter = 0
        
        for contour in sorted_contours:
            x, y, w, h = cv2.boundingRect(contour)
            
            #Recognize each line coordinate and crop the image
            line_image = image[y:y + h, x:x+w]
            counter+=1
            keys=counter
            value=line_image
            text_images[keys]=text_images.setdefault(keys, value)
            

        parag+=1
        key=parag
        values= text_images
        paragraphs[key]=paragraphs.setdefault(key, values)

    return paragraphs


