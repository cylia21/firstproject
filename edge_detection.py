import cv2 as cv 
import numpy as np 


### Modify folder here 
cat_path = "C:/Users/csa/Desktop/github/file/chat.jpg" 


### load image 
file = cv.imread(cat_path, 0) 

### Canny filter 
detector = cv.Canny(file)
