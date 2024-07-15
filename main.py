import os
import pathlib
import cv2
from text_detect.detect_line import Line_detect
from text_detect.detect_paragraph import Paragraph_detect
from text_detect.src.save_images import save_images


folder = f"{pathlib.Path(__file__).resolve().parent}/pics"
def main():
   
   dict1 = {}
   for filename in os.listdir(folder):
      
      
      img = cv2.imread(os.path.join(folder, filename))
   
      list_parag = Paragraph_detect(img)
      dict1["{}".format(filename)] = Line_detect(list_parag)
      
   save_images(dict1)
      
   


if __name__=="__main__":
   
   main()