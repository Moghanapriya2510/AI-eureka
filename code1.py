import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('flower.jpg',cv2.IMREAD_ANYCOLOR)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
