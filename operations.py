import math
from scipy.spatial import distance as dist
import numpy as np

class Operations:
    def PointsPosition(i, edge, step_len):
        x1 = edge[0][0]
        x2 = edge[1][0]
        y1 = edge[0][1]
        y2 = edge[1][1]
        dx = x2 - x1
        dy = y2 - y1
        len = math.sqrt(dx * dx + dy * dy)
        udx = dx / len
        udy = dy / len
        x = int(x1 + udx * (i + 1) * step_len)
        y = int(y1 + udy * (i + 1) * step_len)
        return x, y

    def GetIndexes(counturClass, x0, x1, y0, y1):
        A = y0 - y1
        B = x1 - x0
        C = x0 * y1 - x1 * y0

        # print('============================')
        # print('x0, y0: ({}, {})\nx1, y1: ({}, {})\nA = {}, B = {}, C = {}'.format(x0, y0, x1, y1, A, B, C))
        # print('============================')

        a = []
        for point in counturClass.countur:                                  # изменить перебор на поиск с условием/ фильтр?
            a.append(math.fabs(A * point[0][0] + B * point[0][1] + C))
        #print(a)

        ind1 = a.index(min(a))
        #print(a[ind1], ind1, counturClass.countur[ind1][0])
        a.pop(ind1)
        while True:
            ind2 = a.index(min(a))
            if dist.euclidean(counturClass.countur[ind1][0],
                              counturClass.countur[ind2][0]) < 50:  # ПЕРЕСМОТРЕТЬ УСЛОВИЕ ПРОВЕРКИ
                a.pop(ind2)
                continue
            else:
                #print(a[ind2], ind2, counturClass.countur[ind2][0])
                break
        return ind1, ind2

    def order_points(pts):
        rect = np.zeros((4, 2), dtype="float32")  # list of coordinates
        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]  # the top-left point will have the smallest sum
        rect[2] = pts[np.argmax(s)]  # the bottom-right point will have the largest sum

        diff = np.diff(pts, axis=1)  # difference between the points
        rect[1] = pts[np.argmin(diff)]  # top-right point will have the smallest difference,
        rect[3] = pts[np.argmax(diff)]  # bottom-left will have the largest difference

        return rect