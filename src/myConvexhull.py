# File implementasi Convex hull dengan divide & conquer
import numpy as np 
def determinantThreePoints(p1, p2, pi):
    # Mengembalikan determinan dari tiga titik koordinat
    return (p1[0] * p2[1] + pi[0] * p1[1] + p2[0] * pi[1] - pi[0] * p2[1] - p2[0] * p1[1] - p1[0] * pi[1])

def up(p1, p2, pi):
    return (determinantThreePoints(p1, p2, pi) > 0)


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