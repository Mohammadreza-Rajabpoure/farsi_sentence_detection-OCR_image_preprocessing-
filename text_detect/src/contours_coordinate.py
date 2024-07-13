'''
In this function we detect centroid coordinates of contours on X axi using cv2.moments() function
'''
import cv2

def Ret_x_coordinate(contour):
  if cv2.contourArea(contour) > 10 :
    centroid_moment = cv2.moments(contour)
    center = (int(centroid_moment['m10']/centroid_moment['m00']))
    return center
  else:
    pass