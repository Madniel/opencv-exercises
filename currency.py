# Coins of denomination 5 zloty and 1 gr are placed in the picture. Determine the number of each type of coin and label it
# by a colored border on the picture (red for the coins of 5 zloty and green for the coins of 1 gr).
import cv2
import numpy as np


def currency(path):
    img = cv2.imread(path)

    img_tmp = img.copy()
    img_tmp_gray = cv2.cvtColor(img_tmp, cv2.COLOR_BGR2GRAY)

    img_tmp_gray = cv2.medianBlur(img_tmp_gray, ksize=11)
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    img_tmp_gray = cv2.filter2D(img_tmp_gray, -1, kernel)

    circles = cv2.HoughCircles(img_tmp_gray, cv2.HOUGH_GRADIENT, 1, 10,
                               param1=50, param2=50, minRadius=45, maxRadius=70)
    circles = np.uint16(np.around(circles))

    number_5 = 0
    for i in circles[0, :]:
            cv2.circle(img_tmp, (i[0], i[1]), i[2], (0, 0, 255), 5)
            cv2.circle(img_tmp, (i[0], i[1]), 2, (0, 0, 255), 5)
            number_5 += 1

    circles = cv2.HoughCircles(img_tmp_gray, cv2.HOUGH_GRADIENT, 1, 10,
                               param1=50, param2=50, minRadius=0, maxRadius=40)
    circles = np.uint16(np.around(circles))

    number_1 = 0
    for i in circles[0, :]:
            cv2.circle(img_tmp, (i[0], i[1]), i[2], (255, 0, 0), 5)
            cv2.circle(img_tmp, (i[0], i[1]), 2, (255, 0, 0), 5)
            number_1 += 1

    print(number_5)
    print(number_1)
    cv2.namedWindow('Currency')
    cv2.imshow('Currency', img_tmp)
    cv2.waitKey()


if __name__ == '__main__':
    file = 'data/currency.png'
    currency(file)
