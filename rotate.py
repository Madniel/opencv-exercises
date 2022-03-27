# Display the loaded color image in a window; add mouse support to the window.
# Click the left button to rotate the of the four image fragments created by passing a horizontal and vertical line through the clicked point.
# Clicking anywhere with the right key resets the layout and returns to the original image.
import cv2

clear = False
saved_points = []

def rotate(path):
    global clear
    global saved_points

    def save_point(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            global saved_points
            saved_points = x, y
        elif event == cv2.EVENT_RBUTTONDOWN:
            global clear
            clear = True

    img = cv2.imread(path)
    cv2.namedWindow('Rotate')
    cv2.setMouseCallback('Rotate', save_point)
    cv2.imshow('Rotate', img)
    img_tmp = img.copy()

    h, w = img.shape[:2]
    key = ord(' ')

    while key != ord('q'):
        if saved_points:
            x, y = saved_points

            img1 = img_tmp[0:y, 0:x]
            img1_r = img1.shape[:2][::-1]

            img2 = img_tmp[0:y, x:w]
            img2_r = img2.shape[:2][::-1]

            img3 = img_tmp[y:h, x:w]
            img3_r = img3.shape[:2][::-1]

            img4 = img_tmp[y:h, 0:x]
            img4_r = img4.shape[:2][::-1]

            img1_x = cv2.resize(img4, img1_r)
            img2_x = cv2.resize(img1, img2_r)
            img3_x = cv2.resize(img2, img3_r)
            img4_x = cv2.resize(img3, img4_r)

            img_tmp[0:y, 0:x] = img1_x
            img_tmp[0:y, x:w] = img2_x
            img_tmp[y:h, x:w] = img3_x
            img_tmp[y:h, 0:x] = img4_x

            saved_points = []

        if clear:
            img_tmp = img.copy()
            print('Orginal photo')
            clear = False
        cv2.imshow('Rotate', img_tmp)
        key = cv2.waitKey(1)


if __name__ == '__main__':
    file = 'data/flowers.jpg'
    rotate(file)
