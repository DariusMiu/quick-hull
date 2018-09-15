import matplotlib
import Point
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
import random
import math
from numpy import arccos, array, dot, pi, cross
from numpy.linalg import det, norm

filename = 'plot'
rand = random.seed()

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

def findhull(points, p, q) :
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
	print("p:" + str(convexhull[p]) + " q:" + str(convexhull[q]) + " c:" + str(convexhull[c]))
	findhull(S1, p, c)
	findhull(S2, c, q)
#

p = []
convexhull = []
convexhulltop = []

for i in range(50) :
	p.append(Point.Point(i,random.randint(0, 20), 'y'))

convexhull.append(p[0])
convexhull.append(p[len(p)-1])
convexhulltop.append(p[0])
convexhulltop.append(p[len(p)-1])

top = []
bottom = []

for i in range(1,len(p) - 1) :
	if side(p[0], p[len(p)-1], p[i]) > 0 :
		p[i].color = 'r'
		top.append(p[i])
	if side(p[len(p)-1], p[0], p[i]) > 0 :
		p[i].color = 'b'
		bottom.append(p[i])

drawline(convexhull[0], convexhull[1], 'g--', 1)

print("len(p):" + str(len(p)) + " len(top+bottom):" + str(len(top) + len(bottom)))
print("len(top):" + str(len(top)) + " len(bottom):" + str(len(bottom)))
print("top:")
for i in range(len(top)) :
	print(str(top[i]), end=' ')
print()
print("bottom:")
for i in range(len(bottom)) :
	print(str(bottom[i]), end=' ')
print()
print()

print("initial:")
for i in range(len(convexhull)) :
	print(str(convexhull[i]), end=' ')
print()
findhull(bottom, len(convexhull)-1, 0)
print("second half:")
for i in range(len(convexhull)) :
	print(str(convexhull[i]), end=' ')
print()
drawloc = len(convexhull) - 1
findhull(top, 0, len(convexhull)-1)
print("final:")
for i in range(len(convexhull)) :
	print(str(convexhull[i]), end=' ')
print()


#for i in range(len(p)) :
#	plt.plot(p[i].X, p[i].Y, 'yo', markersize=2)
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





















