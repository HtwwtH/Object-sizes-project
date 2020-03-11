import cv2
import numpy as np

def Show(img1):
    cv2.namedWindow("window", cv2.WINDOW_NORMAL)
    cv2.imshow("window", img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

class ImageProcessing:
    def ImageProc(ImgIn):
        img = ImgIn
        t_p = 15
        img = cv2.bilateralFilter(img, t_p, 15, 15)
        kernel = np.array([
            [0.200, 0.200, 0.200],
            [0.200, 0.200, 0.200],
            [0.200, 0.200, 0.200]
        ])
        img = cv2.filter2D(img, -1, kernel)

        kernel = np.ones((3, 3), np.uint8)
        img = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel, iterations=1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (_, img) = cv2.threshold(img, 250, 255, cv2.THRESH_BINARY)
        kernel = np.ones((3, 3), np.uint8)
        img = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel, iterations=2)
        img = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel, iterations=1)

        img = cv2.bitwise_not(img)
        Show(img)

        return img


    def imageBook(imgIn):
        img = imgIn

        kernel = np.array([[0.400 for i in range(3)] for j in range(3)])
        img = cv2.filter2D(img, -1, kernel)
        #Show(img)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (3, 3), 0)
        img = cv2.equalizeHist(img)
        #Show(img)

        #(_, img) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        ret3, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        kernel = np.ones((3, 3), np.uint8)
        img = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel, iterations=3)
        img = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel, iterations=2)

        #Show(img)

        #img = cv2.bitwise_not(img)

        return img