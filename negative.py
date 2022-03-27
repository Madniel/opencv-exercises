# Display the loaded color image in a window;
# add a slider to the window.
# Moving the slider determines which part of the displayed
# e.g. extreme left position - image unchanged,
# extreme right position - image unchanged
# - the negative image itself,
# halfway position - left 50% of the image unchanged,
# right 50% of the image negative.
# The whole image should change smoothly, depending on the position of the slider.

import cv2


def negative(path):
    def empty_callback():
        pass

    img = cv2.imread(path)
    cv2.namedWindow('negative')
    cv2.createTrackbar('slider', 'negative', 0, 100, empty_callback)

    w, h = img.shape[:2]

    key = ord(' ')
    while key != ord('q'):
        img_tmp = img.copy()
        value = cv2.getTrackbarPos('slider', 'negative')
        value = int((value * w) / 100)
        for i in range(h):
            for j in range(w):
                if j < value:
                    img_tmp[i][j][0] = 255 - img_tmp[i][j][0]
                    img_tmp[i][j][1] = 255 - img_tmp[i][j][1]
                    img_tmp[i][j][2] = 255 - img_tmp[i][j][2]

        cv2.imshow('negative', img_tmp)
        cv2.waitKey(1)


if __name__ == '__main__':
    file = 'data/flowers.jpg'
    negative(file)
