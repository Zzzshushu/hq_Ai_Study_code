import numpy as np

# 使用OpenCV库来进行查看图像及其他操作
import cv2

# 使用matplotlib库来一次性展示多个图像
import matplotlib.pyplot as plt

# 创建一个700 * 700 的三维数组（彩色图）
# 使用np.zeros创建一个数值全为0的数组，对应一张黑色图
# uint8: unsigned int 无符号整数 0-255
image = np.zeros((7, 7, 3), dtype=np.uint8)
print(image)
cv2.imshow('image', image)

cv2.waitKey(0)
for i in range(0, 7, 1):  # i: 0, 100, 200, 300, 400, 500, 600
    for j in range(0, 7, 1):  # j: 0, 100, 200, 300, 400, 500, 600
        image[i, :, :] = 255  # 修改第i行的所有像素
        image[:, j, :] = 255  # 修改第j列的所有像素
print(image)    