import matplotlib
import Point
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
import random
import math
from numpy import arccos, array, dot, pi, cross
from numpy.linalg import det, norm
import sys

filename = 'plot'
rand = random.seed()

def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
#

def drawline(p1, p2, style, width) :
	plt.plot([p1.X,p2.X],[p1.Y,p2.Y], style, linewidth=width)
#

#https://stackoverflow.com/questions/849211/shortest-distance-between-a-point-and-a-line-segment?page=1&tab=votes#tab-top
def distSQR(p1, p2, p): # p is the point
    px = p2.X-p1.X
    py = p2.Y-p1.Y

    something = px*px + py*py

    u =  ((p.X - p1.X) * px + (p.Y - p1.Y) * py) / float(something)

    if u > 1:
        u = 1
    elif u < 0:
        u = 0

    x = p1.X + u * px
    y = p1.Y + u * py

    dx = x - p.X
    dy = y - p.Y

    return dx*dx + dy*dy
#

def dist(p1, p2, p): # p is the point
	return math.sqrt(distSQR(p1, p2, p))
#

def contains(p1, p2, p3, p) :
	alpha = ((p2.Y - p3.Y)*(p.X - p3.X) + (p3.X - p2.X)*(p.Y - p3.Y)) / ((p2.Y - p3.Y)*(p1.X - p3.X) + (p3.X - p2.X)*(p1.Y - p3.Y));
	beta = ((p3.Y - p1.Y)*(p.X - p3.X) + (p1.X - p3.X)*(p.Y - p3.Y)) / ((p2.Y - p3.Y)*(p1.X - p3.X) + (p3.X - p2.X)*(p1.Y - p3.Y));
	gamma = 1 - alpha - beta;
	if alpha > 0 and beta > 0 and gamma > 0 :
		return True
	else :
		return False
#

def side(A, B, P) :
	return (B.X - A.X) * (P.Y - A.Y) - (B.Y - A.Y) * (P.X - A.X)
#

def findhull(points, p, q, top) :
	global convexhull
	#convexhull[p],convexhull[q] = dividing line segment
	if len(points) <= 0 :
		return
	f = -1
	c = -1
	for i in range(len(points)) :
		d = dist(convexhull[p], convexhull[q], points[i])
		#print("distance[" + str(i) + "]:" + str(d))
		if (d > f) :
			f = d
			c = i
	if p > q :
		convexhull.insert(p, points[c])
		pointc = points.pop(c)
		c = p
		p = p + 1
	else :
		convexhull.insert(q, points[c])
		pointc = points.pop(c)
		c = q
		q = q + 1
	#S0=[]
	S1=[]
	S2=[]
	for i in range(len(points)) :
		if not contains(convexhull[p],convexhull[q],pointc,points[i]) : #ignore if the triangle contains it
			if side(convexhull[p], pointc, points[i]) > 0 :
				S1.append(points[i])
			if side(pointc, convexhull[q], points[i]) > 0 :
				S2.append(points[i])
	#print("p:" + str(convexhull[p]) + " q:" + str(convexhull[q]) + " c:" + str(convexhull[c]))
	if top :
		findhull(S2, c, q, top)
		findhull(S1, p, c, top)
	else :
		findhull(S1, p, c, top)
		findhull(S2, c, q, top)
#

points = []
convexhull = []

size = 50
if len(sys.argv) > 1 and is_int(sys.argv[1]) :
	size = int(sys.argv[1])

for i in range(size) :
	points.append(Point.Point(i,random.randint(0, size), 'y'))

convexhull.append(points[0])
convexhull.append(points[len(points)-1])

top = []
bottom = []

for i in range(1,len(points) - 1) :
	if side(points[0], points[len(points)-1], points[i]) > 0 :
		points[i].color = 'r'
		top.append(points[i])
	if side(points[len(points)-1], points[0], points[i]) > 0 :
		points[i].color = 'b'
		bottom.append(points[i])

drawline(convexhull[0], convexhull[1], 'g--', 0.5)

print("len(points):" + str(len(points)))
print("len(top):" + str(len(top)) + " len(bottom):" + str(len(bottom)))


findhull(top, 0, len(convexhull)-1, True)
drawloc = len(convexhull) - 1
findhull(bottom, len(convexhull)-1, 0, False)


print("len(convexhull):" + str(len(convexhull)))


#for i in range(len(points)) :
#	plt.plot(points[i].X, points[i].Y, 'yo', markersize=2)
for i in range(len(top)) :
	plt.plot(top[i].X, top[i].Y, top[i].color + 'o', markersize=2)
for i in range(len(bottom)) :
	plt.plot(bottom[i].X, bottom[i].Y, bottom[i].color + 'o', markersize=2)
for i in range(len(convexhull)) :
	plt.plot(convexhull[i].X, convexhull[i].Y, 'go', markersize=3)
for i in range(drawloc - 1) :
	drawline(convexhull[i], convexhull[i+1], 'g-', 0.5)
drawline(convexhull[drawloc - 1], convexhull[len(convexhull) - 1], 'g-', 0.5)
for i in range(drawloc, len(convexhull) - 1) :
	drawline(convexhull[i], convexhull[i+1], 'g-', 0.5)
#drawline(convexhull[drawloc], convexhull[len(convexhull) - 1], 'g-', 0.5)
drawline(convexhull[drawloc], convexhull[0], 'g-', 0.5)


plt.draw()
plt.savefig(filename, dpi=300)
print("successfully exported " + filename + ".png")
plt.show()





















