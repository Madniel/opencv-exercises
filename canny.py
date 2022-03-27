# Use the mouse on any image - create a rectangle with two clicks, and then inside the rectangle perform the
# edge finding operation using Canny's algorithm.
import cv2


def canny(path):
    points = []

    def save_point(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            points.append((x, y))
        elif event == cv2.EVENT_MBUTTONDOWN:
            print('Point cleared')
            points.clear()

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img_tmp = img.copy()

    cv2.namedWindow('canny')
    cv2.setMouseCallback('canny', save_point)

    key = ord(' ')
    while key != ord('q'):
        if len(points) == 2:
            p_1 = points[0][1], points[1][1]
            p_2 = points[0][0], points[1][0]

            img_tmp_2 = img_tmp[p_1[0]:p_1[1], p_2[0]:p_2[1]]
            img_tmp_2 = cv2.Canny(img_tmp_2, 100, 100)
            img[p_1[0]:p_1[1], p_2[0]:p_2[1]] = img_tmp_2
            points = []

        cv2.imshow('canny', img)
        cv2.waitKey(1)


if __name__ == '__main__':
    file = 'data/doge.png'
    canny(file)
