import numpy as np
import cv2

net = cv2.dnn.readNet('yolov3-tiny.weights', 'yolov3-tiny.cfg')
classes = []
with open('coco.names', 'r') as f:
    classes = f.read().splitlines()

img = cv2.imread('image.jpg')
height, width, _ = img.shape
blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
for b in blob:
    for n, img_blob in enumerate(b):
        cv2.imshow(str(n), img_blob)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()