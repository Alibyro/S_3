import cv2
import numpy as np

image =  cv2.imread("lion.jpg", cv2.IMREAD_GRAYSCALE)

width=image.shape[0]
height=image.shape[1]

kernel = np. array([[1,0,-1],
                    [-1,4,-1],
                    [0,-1,0]])

result = np.zeros((width, height), dtype=np.uint8)

for i in range (1, width-1):
    for j in range(1, height-1):
        small_image = image[i-1:i+2, j-1:j+2]
        output = np.multiply(small_image, kernel)
        out = np.sum(output)
        result[i,j]=out
        
cv2.imshow("output", result)
cv2.waitKey()