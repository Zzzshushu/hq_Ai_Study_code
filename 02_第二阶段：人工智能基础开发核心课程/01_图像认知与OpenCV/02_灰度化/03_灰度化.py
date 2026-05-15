import cv2
import numpy as np

image_np = cv2.imread('flower.png')

cv_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

image_shape = image_np.shape
image_gray = np.zeros((image_shape[0], image_shape[1]), dtype=np.uint8)

weight_red = 0.299
weight_green = 0.587
weight_blue = 0.114

for i in range(image_shape[0]):
    for j in range(image_shape[1]):
        # 遍历到所有的像素点之后，开始进行加权平均的计算
        image_gray[i][j] = round(image_np[i, j][0] * weight_blue + image_np[i, j][1] * weight_green \
                                 + image_np[i, j][2] * weight_red)
print('使用opencv的结果：', cv_gray)

print('=' * 100)

print('自己手动计算的结果：', image_gray)

# cv2.imshow('cv_gary', cv_gray)
cv2.imshow('image_np', image_np)
cv2.imshow('image_gray', image_gray)

cv2.waitKey(0)
