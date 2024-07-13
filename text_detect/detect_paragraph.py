'''
In this function we decide to detect and crop each paragraph(here clones of farsi texts)
from the image with image background ,
the input is an image and the output is a list of the images for each paragraph

 1st >> (line 37) >> make a copy of image to work with it

 2nd >> (line 40) >> use Threshold() function from src.threshold to detect all the text pixels

 3nd >> (line 42) >> set a kernel of(5,5) with cv2.getStructuringElement() to detect the words,
dots,numbers,characters,...from Thresholded image 

 4nd >> (line 45) >> connect all the words and lines in a paragraph using rect_kernel by iteration of
 10 pixels

 5nd >> (line 48) >> set a contour for each paragraph using cv2.findContours and dilated image
 
 6nd >> (line 51) >> filter the contours to pic large ones by cv2.arcLength() that gives us 
 the contour's perimeter 

 6nd >> (line 54) >> sort contours from rigth to left using Ret_x_coordinate

 7nd >> (line 56 to 63) >> find each contour coordinate on and assigne it to the image to crop the paragraph
 and append to a list

'''

import cv2
import numpy as np
from text_detect.src.contours_coordinate import Ret_x_coordinate
from text_detect.src.threshold import Threshold

def Paragraph_detect(image):

    duplicate_image = image.copy() #make a copy of image
                                     
    all = Threshold(duplicate_image) #detect the texts from image
    
    #set a rectangular kernel to containe all alphabets character and words of a text line such as dots,numbers,...
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    #connect the words by iteration 10 pixels
    dilation = cv2.dilate(all, rect_kernel, iterations = 10)
    
    #find contours of each paragraph
    contours, _ = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    #filter the large contours
    filtered_contours = [cnt for cnt in contours if cv2.arcLength(cnt,True)>=1000]

    #sorting contours from right to left 
    sorted_contours = sorted(filtered_contours, key=Ret_x_coordinate, reverse=True) 
    
    text_paragraps = []
    for contour in sorted_contours:
       x, y, w, h = cv2.boundingRect(contour) #find the contours coordinates
    
       #Recognize each paragraph and Crop the paragraph from original image
       paragraph = image[y:y + h, x:x+w]
       
       text_paragraps.append(paragraph)

    return text_paragraps