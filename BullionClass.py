import cv2
import imutils
import numpy as np
from scipy.spatial import distance as dist
from morf import ImageProcessing
from operations import Operations

class CounturClass:
    def __init__(self):
        self.countur = None
        self.box = []

        self.len1_points = []
        self.len2_points = []
        self.wid1_points = []
        self.wid2_points = []

        self.len_c_points = []
        self.wid_c_points = []


class Bullion():
    def __init__(self, img_name):
        self.k = 0.2142857

        self.img_name = img_name
        self.img = None
        self.bw_img = None
        self.img_processed = None
        self.lens = 0
        self.widths = 0

        self.counturClass=CounturClass()

        self.browse_images()



    def browse_images(self):
        img = cv2.imread(self.img_name)
        if img is not None:
            self.img = img
            self.img_processed = img
            self.bw_img = ImageProcessing.imageBook(self.img)

    def drawContours(self):
        img = self.img_processed.copy()
        self.getBoxData()
        cv2.drawContours(img, self.counturClass.countur, -1, (145, 255, 145), 2)
        self.img_processed = img

    def measureJustEdges(self, img):
        (tl, tr, br, bl) = self.counturClass.box
        _Wtop = round(dist.euclidean(tl, tr)*self.k,1)
        _Hright = round(dist.euclidean(tr, br)*self.k,1)

        cv2.putText(img, str(_Wtop), (tl[0], tl[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img, str(_Hright), (tr[0], int(tr[1] + 35)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),2)
        return img

    def getBoxData(self):
        img = self.img_processed.copy()
        bwimg = self.bw_img.copy()
        thresh = cv2.threshold(bwimg, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        contours = contours[0] if imutils.is_cv2() else contours[1]

        for contour in contours:
            # Get the rectangle that contains the contour
            (x, y, w_tmp, h_tmp) = cv2.boundingRect(contour)

            if w_tmp >= h_tmp:
                w = w_tmp
                h = h_tmp
            else:
                w = h_tmp
                h = w_tmp

            if h > 50 and w > 50:  # ПЕРЕСМОТРЕТЬ УСЛОВИЕ ПРОВЕРКИ
                peri = cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, 0.04 * peri, True)

                if len(approx) == 4:
                    box = cv2.minAreaRect(contour)
                    box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
                    box = np.array(box, dtype="int")

                    self.counturClass.countur = contour
                    self.counturClass.box = Operations.order_points(box)

                    break

    def drawRectangle(self):
        self.getBoxData()
        img = self.img_processed.copy()
        cv2.drawContours(img, [self.counturClass.box.astype("int")], -1, (255, 0, 0), 1)
        img = self.measureJustEdges(img)
        self.img_processed = img


    def clearBullion(self):
        self.img_processed = self.img
        self.counturClass = CounturClass()

    def lines(self, command):
        self.getBoxData()
        (tl, tr, br, bl) = self.counturClass.box

        if dist.euclidean(tl,bl)>dist.euclidean(tl,tr):
            len1 = (tl, bl)
            len2 = (tr, br)
            wid1 = (tl, tr)
            wid2 = (bl, br)

        else:
            len1 = (tl, tr)
            len2 = (bl, br)
            wid1 = (tl, bl)
            wid2 = (tr, br)

        self.fillPoints('len', len1, len2, self.lens)
        self.fillPoints('wid', wid1, wid2, self.widths)
        if command is 'rect':
            self.rectPoints()
        else:
            self.contourPoints()

    def fillPoints(self, command, edge1, edge2, measures):
        step = int(dist.euclidean(edge1[0], edge1[1]) / (measures + 1))
        for i in range(measures):
            x0, y0 = Operations.PointsPosition(i, edge1, step)
            if command is 'len':
                self.counturClass.len1_points.append((x0, y0))
            else:
                self.counturClass.wid1_points.append((x0, y0))

            x1, y1 = Operations.PointsPosition(i, edge2, step)
            if command is 'len':
                self.counturClass.len2_points.append((x1, y1))
            else:
                self.counturClass.wid2_points.append((x1, y1))

            ind1, ind2 = Operations.GetIndexes(self.counturClass, x0, x1, y0, y1)

            if command is 'len':
                self.counturClass.len_c_points.append(
                    [(self.counturClass.countur[ind1][0][0], self.counturClass.countur[ind1][0][1]),
                     (self.counturClass.countur[ind2][0][0], self.counturClass.countur[ind2][0][1])])
            else:
                self.counturClass.wid_c_points.append(
                    [(self.counturClass.countur[ind1][0][0], self.counturClass.countur[ind1][0][1]),
                     (self.counturClass.countur[ind2][0][0], self.counturClass.countur[ind2][0][1])])

    def rectPoints(self):
        img = self.img_processed.copy()
        for point in self.counturClass.len1_points:
            x0, y0 = point
            cv2.circle(img, (x0, y0), 3, (0, 0, 255), -1)

        for point in self.counturClass.wid1_points:
            x0, y0 = point
            cv2.circle(img, (x0, y0), 3, (0, 0, 255), -1)

        for point in self.counturClass.len2_points:
            x1, y1 = point
            cv2.circle(img, (x1, y1), 3, (0, 0, 255), -1)

        for point in self.counturClass.wid2_points:
            x1, y1 = point
            cv2.circle(img, (x1, y1), 3, (0, 0, 255), -1)

        self.img_processed = img


    def contourPoints(self):
        img = self.img_processed.copy()
        for item in self.counturClass.len_c_points:
            for point in item:
                cv2.circle(img, point, 3, (0, 100, 0), -1)
        for item in self.counturClass.wid_c_points:
            for point in item:
                cv2.circle(img, point, 3, (0, 100, 0), -1)


        self.img_processed = img


    def measureExplore(self):
        widths = []
        for pair in self.counturClass.len_c_points:
            w = round(dist.euclidean(pair[0], pair[1])*self.k,1)
            widths.append(w)

        lengths = []
        for pair in self.counturClass.wid_c_points:
            l = round(dist.euclidean(pair[0], pair[1])*self.k,1)
            lengths.append(l)

        return widths, lengths

    def drawLines(self):
        img = self.img_processed.copy()
        for pair in self.counturClass.len_c_points:
            cv2.line(img, pair[0], pair[1], (0, 255, 0), 1)
        for pair in self.counturClass.wid_c_points:
            cv2.line(img, pair[0], pair[1], (0, 255, 0), 1)
        self.img_processed = img