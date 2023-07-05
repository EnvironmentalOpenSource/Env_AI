import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Open source repository, developed by Built Environment Lab, IIT Gandhinagar.

# Original author: Ashwini Ramanuj, ashwiniramanuj1801@gmail.com
# Date created: 2021/05/20
# Last modified: 2021/05/20

class BuildingsAnalyzer:
    def __init__(self):
        """
        This class is used to detect buildings in an image.
        """
        pass
     
    def generate_boxes(self, image_path:str=None,dir_path:str=None,image_format:list or str=None,save_images=False, save_dir_path:str=None):
        """

        This function is used to generate bounding boxes around buildings in an image.

        Parameters:
            image_path: str
            dir_path: str
            image_format: list or str
            save_images: bool
            save_dir_path: str
        """
        if image_path:
            image = cv2.imread(image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Perform image segmentation using a thresholding technique
            _, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
            
            # Find contours of the segmented regions
            contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Draw bounding boxes around the segmented regions on the original image
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)
            
            # Display the original image with yellow bounding boxes
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            plt.figure(figsize=(8, 8))
            plt.imshow(image)
            plt.title(image_path+" with Bounding Boxes")
            plt.axis("off")
            plt.show()

            if save_images:
                    if save_dir_path:
                        cv2.imwrite(save_dir_path+"/"+image_name,image)
                    else:
                        print("Please provide save_dir_path")

        elif dir_path:
            image_names=[]
            with os.scandir(dir_path) as entries:
                for entry in entries:
                    if type(image_format) == str:
                        image_names.append(entry.name) if entry.name.endswith(image_format) else None
                    elif type(image_format) == list:
                        image_names.append(entry.name) if entry.name.endswith(tuple(image_format)) else None
            for image_name in image_names:
                image = cv2.imread(dir_path+"/"+image_name)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                
                # Perform image segmentation using a thresholding technique
                _, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
                
                # Find contours of the segmented regions
                contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                
                # Draw bounding boxes around the segmented regions on the original image
                for contour in contours:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)
                
                # Display the original image with yellow bounding boxes
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                plt.figure(figsize=(8, 8))
                plt.imshow(image)
                plt.title(image_name+" with Bounding Boxes")
                plt.axis("off")
                plt.show()

                if save_images:
                    if save_dir_path:
                        cv2.imwrite(save_dir_path+"/"+image_name,image)
                    else:
                        print("Please provide save_dir_path")
        
        else:
            print("Please provide either image_path or dir_path") 