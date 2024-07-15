import cv2
import pathlib
import os

storeg_path = os.path.abspath('storeg')
dict_of_images:dict
def save_images(dict_of_images:dict):
    
   image_names=list(dict_of_images.keys())
   
   for image_name in image_names:
       
       paragraf_numbers = list((dict_of_images[image_name]).keys())
       for parag_num in paragraf_numbers:
           img_numbers = list((dict_of_images[image_name][parag_num]).keys())
           for image_num in img_numbers:
               
               img_name = "{}_{}_sentence num {}".format(str(image_name),
                                                          str(parag_num),
                                                          str(image_num))
               image =dict_of_images[image_name][parag_num][image_num]
               
               image_path = os.path.join(storeg_path, '{}.jpg'.format(img_name))
               
               cv2.imwrite(image_path, image)