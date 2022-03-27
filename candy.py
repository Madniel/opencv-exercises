# Design and implement a method to find a selected type of candy in a provided image.
import cv2
import numpy as np


def candy(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (0, 0), fx=0.7, fy=0.6)

    img_tmp = img.copy()
    img_tmp_gray = cv2.cvtColor(img_tmp, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(img_tmp_gray, cv2.HOUGH_GRADIENT, 1, 10,
                               param1=50, param2=50, minRadius=30, maxRadius=60)
    circles = np.uint16(np.around(circles))

    mask = np.zeros((img_tmp.shape[0], img_tmp.shape[1]), np.uint8)

    for i in circles[0, :]:
        cv2.circle(mask, (i[0], i[1]), i[2] - 3, (255, 255, 255), -1)
        cv2.circle(mask, (i[0], i[1]), i[2] - 8, (0, 0, 0), -1)
        mean_rgb = cv2.mean(img_tmp, mask=mask)[::-1]
        cv2.imshow('mask', mask)
        # cv2.waitKey()
        print(mean_rgb[1])
        if mean_rgb[1] > 220:
            cv2.circle(img_tmp, (i[0], i[1]), i[2], (0, 255, 0), 7)
        mask = np.zeros((img_tmp.shape[0], img_tmp.shape[1]), np.uint8)

    cv2.namedWindow('tmp')
    cv2.imshow('tmp', img_tmp)
    cv2.waitKey()


if __name__ == '__main__':
    file = 'data/candy.jpg'
    candy(file)
