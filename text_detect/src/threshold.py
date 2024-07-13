'''
In this function we are going to seperate all texts in an image to return a numpy.ndarray 
that is a balck image with previos image's texts in white color

1st >>(line 26) >> change image from RGB to Grayscale 

2nd >>(line 28)>> use the threshold_multiotsu() function from skimage.filters to find thresholds 

3nd >>(line 30)>> detect the segments of thresholds by digitizing the image using np.digitize that returns
an image with bined pixels to numbers of threshold's segments(here we have 5 segments(0,1,2,3,4)

4nd >>(line 32 to 36)>> change each area's pixels into boolian type

5nd >>(line 37 to 38)>> binary the areas that containes pixels of segment_1 
(refer to pixels with 0 values(balck pixels)) using ndimage from scipy(nd.binary_opening|_closing) with (1,1) kernel 

6nd >>(line 40 to 41)>> make a black image and assigne the binary pixels to it
'''
import cv2
from scipy import ndimage as nd
import numpy as np
from skimage.filters import threshold_multiotsu

def Threshold(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #chainging image from BGR to Grayscale

    thresholds = threshold_multiotsu(gray, classes=5) #threshold the image to 5 segments
    
    regions  = np.digitize(gray, bins=thresholds) #detect the segments region with binning to thresholds
    
    seg1 = (regions == 0) #change the segment pixels into boolian by specified value
    seg2 = (regions == 1)
    seg3 = (regions == 2)
    seg4 = (regions == 3)
    seg5 = (regions == 4)
    seg1_open = nd.binary_opening(seg1, np.ones((1,1)))  #binary the segment 1 
    seg1_close =nd.binary_closing(seg1_open, np.ones((1,1)))
     
    all = np.zeros((gray.shape[0], gray.shape[1]), np.uint8)
    all[seg1_close] = (255)

    return all