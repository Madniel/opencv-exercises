import cv2
import numpy as np

import time


def ex_1():
    def empty(_):
        pass

    cv2.namedWindow('current_frame')
    # cv2.namedWindow('background')
    # cv2.namedWindow('foreground')

    cv2.createTrackbar('threshold', 'current_frame', 20, 255, empty)

    cap = cv2.VideoCapture('data/movie.mp4')

    img_gray = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)
    img_current = np.copy(img_gray)
    img_background = np.copy(img_gray)
    img_foreground = np.copy(img_gray)

    backSub = cv2.createBackgroundSubtractorMOG2()
    backSub = cv2.createBackgroundSubtractorKNN()

    key = ord(' ')
    while key != ord('q'):
        _, frame = cap.read()
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # fgMask = backSub.apply(frame)

        # background update
        # if key == ord('a'):
        # img_background = np.copy(img_current)
        img_background[img_background < img_current] += 1
        img_background[img_background > img_current] -= 1

        # elif key == ord('x'):
        img_current = np.copy(img_gray)

        img_diff = cv2.absdiff(img_background, img_current)

        kernel = np.ones((5, 5), np.uint8)
        img_closed = cv2.morphologyEx(img_diff, cv2.MORPH_OPEN, kernel)

        t = cv2.getTrackbarPos('threshold', 'current_frame')
        _, img_thresholded = cv2.threshold(img_closed, t, 255, cv2.THRESH_BINARY)
        edged = cv2.Canny(img_thresholded, 100, 255)
        contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        img_current = cv2.cvtColor(img_current, cv2.COLOR_GRAY2BGR)

        for i in range(0, len(contours)):
            if (i % 1 == 0):
                cnt = contours[i]

                x, y, w, h = cv2.boundingRect(cnt)
                if w>20:
                    cv2.rectangle(img_current, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow('current_frame', img_current)
        # cv2.imshow('background', img_background)
        # cv2.imshow('foreground', img_thresholded)
        img_current = cv2.cvtColor(img_current, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('fgMask', fgMask)

        key = cv2.waitKey(20)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    print('Hello lab 10!')
    ex_1()