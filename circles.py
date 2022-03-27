# surround the red circles with a blue border and the blue circles with a red border. Write out the number of red and blue circles.
import cv2
import numpy as np


def circle(path):
    img = cv2.imread(path)

    img_tmp = img.copy()
    img_tmp_gray = cv2.cvtColor(img_tmp, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(img_tmp_gray, cv2.HOUGH_GRADIENT, 1, 10,
                               param1=40, param2=40, minRadius=75, maxRadius=100)
    circles = np.uint16(np.around(circles))

    for i in circles[0, :]:
        r = i[2]
        half_r = int(r / 2)
        for j in range(r):
            for k in range(r):
                if img_tmp[i[1] - half_r + j][i[0] - half_r + k][2] > 230:
                    cv2.circle(img_tmp, (i[0], i[1]), i[2], (255, 0, 0), 7)
                if img_tmp[i[1] - half_r + j][i[0] - half_r + k][0] > 230:
                    cv2.circle(img_tmp, (i[0], i[1]), i[2], (0, 0, 255), 7)

    cv2.namedWindow('Circles')
    cv2.imshow('Circles', img_tmp)
    cv2.waitKey()


if __name__ == '__main__':
    file = 'data/circles.png'
    circle(file)
