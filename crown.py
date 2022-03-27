# Label the jewels of any color you choose in the crown of kings.
import cv2
import numpy as np


def crown(path):
    ## Read
    img = cv2.imread(path)

    ## convert to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    ## mask of green (36,25,25) ~ (86, 255,255)
    # mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
    green = cv2.inRange(hsv, (36, 25, 25), (70, 255, 255))

    cnts, hie = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, cnts, -1, (0, 255, 0), 3)

    cv2.imshow("green", img)
    cv2.waitKey(0)


if __name__ == '__main__':
    file = 'data/crown.jpg'
    crown(file)
