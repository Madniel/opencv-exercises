# Load any color image, select two points with the mouse, and perform a negative operation on the area
# outside the rectangle defined by the clicked points. You should be able to do this operation many times.
import cv2


def color_negative(path):
    points = []

    def save_point(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            points.append((x, y))
        elif event == cv2.EVENT_LBUTTONDOWN:
            points.clear()

    img = cv2.imread(path)
    cv2.namedWindow('color_negative')
    cv2.setMouseCallback('color_negative', save_point)

    img_tmp = img.copy()

    key = ord(' ')
    while key != ord('q'):

        if len(points) == 2:
            part = img_tmp[points[0][1]:points[1][1], points[0][0]:points[1][0]]
            img_tmp = 255 - img_tmp

            img_tmp[points[0][1]:points[1][1], points[0][0]:points[1][0]] = part.copy()
            points = []

        cv2.imshow('color_negative', img_tmp)
        cv2.waitKey(1)


if __name__ == '__main__':
    file = 'data/flowers.jpg'
    color_negative(file)
