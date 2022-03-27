# Calculate the spline of the filter given by the equation in M matrix with the grayscale source image.
# From the result, extract the value of the absolute, scale it to a range of values from 0 to 255, and display it.
import cv2
import numpy as np


def print_image(name, img):
    cv2.namedWindow(name)
    cv2.imshow(name, img)


def scaling(path):
    img = cv2.imread(path)
    print_image('Before filtration', img)

    M = np.array([[0, -1, 0],
                  [-1, 4, -1],
                  [0, -1, 0]])
    filtered = cv2.filter2D(img, -1, M)

    print_image('After filtration', filtered)

    filtered = filtered / np.amax(abs(filtered)) * 255

    print_image('After Scaling', filtered)
    cv2.waitKey()


if __name__ == '__main__':
    file = 'data/doge.png'
    scaling(file)
