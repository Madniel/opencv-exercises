# Change the color of the corresponding parts of the tiger to orange
# (we assume that the gray color throughout the image has the same level).
import cv2


def print_image(name, img):
    cv2.namedWindow(name)
    cv2.imshow(name, img)


def tiger(path):
    def save_point(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(img_tmp[x, y])  # checking grey color value

    img = cv2.imread(path)
    print_image('tiger', img)
    cv2.setMouseCallback('tiger', save_point)

    img_tmp = img.copy()

    for i in range(img_tmp.shape[0]):
        for j in range(img_tmp.shape[1]):
            if img_tmp[i][j][0] == 169:
                img_tmp[i][j] = [0, 127, 254]

    print_image('tiger_color', img_tmp)
    cv2.waitKey()


if __name__ == '__main__':
    file = 'data/tiger.png'
    tiger(file)
