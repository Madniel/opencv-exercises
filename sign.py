# Design and implement a method to find the straight ahead order sign in provided images.
import cv2
import numpy as np


def sign(path):
    img = cv2.imread(path)
    cv2.imshow('final', img)
    cv2.waitKey()
    lower, upper = ([86, 31, 4], [220, 88, 50])

    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    mask = cv2.inRange(img, lower, upper)
    cnts, hie = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(img, cnts, -1, (0, 255, 0), 3)
    cv2.imshow("images", img)
    cv2.waitKey(0)


if __name__ == '__main__':
    file = 'data/sign.jpg'
    sign(file)
