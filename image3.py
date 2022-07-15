#getting the imports
import cv2 as cv
import numpy as np

#reading the image
img = cv.imread('image3.jpg')

#gaussian kernel for sharpenig 
gaussian_blur = cv.GaussianBlur(img,(7,7),2)

#sharpening using addweighted()
sharpened1 = cv.addWeighted(img,1.5, gaussian_blur, -0.5, 0)
sharpened2 = cv.addWeighted(img,3.5, gaussian_blur, -2.5, 0)
sharpened3 = cv.addWeighted(img,7.5, gaussian_blur, -6.5, 0)

#showing the sharpened images
cv.imshow('Sharpened 3', sharpened3)
cv.imshow('Sharpened 2', sharpened2)
cv.imshow('Sharpened 1', sharpened1)
cv.imshow('original', img)
cv.waitKey(0)

