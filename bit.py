# In the provided image, the caption is encoded on the youngest bit.
# Perform operations to modify the image in a way allowing the encoded caption to be read.
import cv2


def print_image(name, img):
    cv2.namedWindow(name)
    cv2.imshow(name, img)


def bit(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    print_image('original', img)

    img_tmp = img.copy()

    for i in range(img_tmp.shape[0]):
        for j in range(img_tmp.shape[1]):
            img_tmp[i][j] = 255 if img_tmp[i][j] & 0x01 == 0 else 0

    print_image('decoded', img_tmp)
    cv2.waitKey()


if __name__ == '__main__':
    file = 'data/doge.png'
    bit(file)
