# File implementasi Convex hull dengan divide & conquer
import numpy as np 
import math
from collections import Iterable

def determinantThreePoints(p1, p2, pi):
    # Mengembalikan determinan dari tiga titik koordinat
    return (p1[0] * p2[1] + pi[0] * p1[1] + p2[0] * pi[1] - pi[0] * p2[1] - p2[0] * p1[1] - p1[0] * pi[1])

def up(p1, p2, pi):
    return (determinantThreePoints(p1, p2, pi) > 0)

def down(p1, p2, pi):
    return (determinantThreePoints(p1, p2, pi) < 0)

def ignoreCoordinate(p1, p2, pi):
    return ((p1[0] * (p2[1] - pi[1]) + p2[0] * (pi[1] - p1[1]) + pi[0] * (p1[1] - p2[1])) == 0)

def getExtremeLeftPoint(bucket):
    minXval = min(bucket[:, 0])
    minXidx = np.where(bucket[:,0]==minXval)
    return bucket[minXidx]

def getExtremeRightPoint(bucket):
    maxXval = max(bucket[:, 0])
    maxXidx = np.where(bucket[:,0] == maxXval)
    return bucket[maxXidx]


def getOuterUpPoints(p1, p2, bucket):
    arrOfOuterPoints = np.zeros((len(bucket),2))
    k = 0
    for i in range(len(bucket)):
        if (not ignoreCoordinate(p1, p2, bucket[i])):
            if up(p1, p2, bucket[i]):
                arrOfOuterPoints[k] = bucket[i]
                k += 1
    arrOfOuterPoints = arrOfOuterPoints[~np.all(arrOfOuterPoints == 0, axis=1)]
    return arrOfOuterPoints

def getOuterDownPoints(p1, p2, bucket):
    arrOfOuterPoints = np.zeros((len(bucket), 2))
    k = 0
    for i in range(len(bucket)):
        if (not ignoreCoordinate(p1, p2, bucket[i])):
            if (down(p1, p2, bucket[i])):
                arrOfOuterPoints[k] = bucket[i]
                k += 1
    arrOfOuterPoints = arrOfOuterPoints[~np.all(arrOfOuterPoints == 0, axis=1)]
    return arrOfOuterPoints


def getDistance(p1, p2, p3):
    return np.abs(np.cross(p2-p1, p3-p1)/np.linalg.norm(p2-p1))

def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang



def getMaxPoint(p1, p2, point):
    # Inisialisasi array untuk menyimpan jarak semua titik
    arrOfDistance = [0 for i in range(len(point))]
    for i in range(len(point)):
        arrOfDistance[i] = getDistance(p1, p2, point[i])
    maxDistance = max(arrOfDistance)
    # Cek apakah titik dengan jarak maksimum ada lebih dari satu
    arrOfMax = [i for i, value in enumerate(arrOfDistance) if value == maxDistance]
    if (len(arrOfMax) > 1):
        angle = [0 for i in range(len(arrOfMax))]
        for i in range(len(arrOfMax)):
            angle[i] = getAngle(point[arrOfMax[i]], p1, p2)
        maxIdx = angle.index(max(angle))
        return point[arrOfMax[maxIdx]]
    else:
        return point[arrOfMax[0]]

def convexHull(p1, p2, arrOfPoints):
    
    if (len(arrOfPoints) <= 1):
        if (len(arrOfPoints) == 1): 
            return arrOfPoints 
        else:
            return 0
    else:
        p3 = getMaxPoint(p1,p2, arrOfPoints)
        a = getOuterUpPoints(p1, p3, arrOfPoints)
        b = getOuterUpPoints(p3, p2, arrOfPoints)
        return convexHull(p1, p3, a), p3, convexHull(p3, p1, b)

    
def convertToLinear(list):
    for item in list:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for x in convertToLinear(item):
                yield x
        else:        
            yield item

def myConvexHull(bucket):
    arrOfPoints = []
    p1 = getExtremeLeftPoint(bucket)
    p2 = getExtremeRightPoint(bucket)
    p1new = p1.flatten()
    p2new = p2.flatten()
    upPoints = getOuterUpPoints(p1new,p2new, bucket)
    downPoints = getOuterDownPoints(p1new, p2new, bucket)
    arrOfPoints.append(p1new)
    s1 = convexHull(p1new, p2new, upPoints)
    s2 = convexHull(p2new, p1new, downPoints)
    arrOfPoints.append(s1)
    arrOfPoints.append(p2new)
    arrOfPoints.append(s2)
    temp = []
    for i in range(len(arrOfPoints)):
        temp.append(arrOfPoints[i])
    newtemp = convertToLinear(temp)
    newtemp = [i for i in newtemp if i != 0]
    coordinate = []

    k = 0
    for i in range(len(newtemp)//2):
        coordinate.append([])
        for j in range(2):
            coordinate[i].append(newtemp[k])
            k+=1
    return coordinate

