import sys, os
if os.getcwd().endswith('python-rectangles'):
    sys.path.insert(0, os.path.abspath('.'))
elif os.getcwd().endswith('python-rectangles/tests'):
    sys.path.insert(0, os.path.abspath('..'))
from geometry import *
import math

# ---------------------------- Test Points -----------------------------

p1=Point(10, 20)
p2=Point(10, 20)
p3=Point(20, 30)
p4=Point(20, 30)
assert p1==p2
assert p1!=p3
assert p2!=p3

# --- Point in rect ---
r=Rect(0, 0, 1, 1)
assert r.is_point_inside_rect(Point(1, 0))
assert r.is_point_inside_rect(Point(1, 1))
assert not r.is_point_inside_rect(Point(-1, -1))
assert not r.is_point_inside_rect(Point(-1, 0))
assert not r.is_point_inside_rect(Point(-1, 1))
assert not r.is_point_inside_rect(Point(0, -1))
assert     r.is_point_inside_rect(Point(0, 0))
assert     r.is_point_inside_rect(Point(0, 1))
assert not r.is_point_inside_rect(Point(1, -1))
assert     r.is_point_inside_rect(Point(1, 0))
assert     r.is_point_inside_rect(Point(1, 1))
assert not r.is_point_inside_rect(Point(2, -1))
assert not r.is_point_inside_rect(Point(2, 0))
assert not r.is_point_inside_rect(Point(2, 1))
assert not r.is_point_inside_rect(Point(-1, -1))
assert not r.is_point_inside_rect(Point(-1, 0))
assert     r.is_point_inside_rect(Point(0.5, 0.5))

# --- Distance ---
assert Point(0, 0).distance_to_point(Point(0, 1))==1
assert Point(0, 0).distance_to_point(Point(1, 0))==1
assert Point(0, 0).distance_to_point(Point(1, 1))==math.sqrt(2)
assert Point(0, 2).distance_to_point(Point(1, 1))==math.sqrt(2)
assert Point(0, 0).distance_to_point(Point(20, 20))==math.sqrt(20**2+20**2)
assert Point(20, 20).distance_to_point(Point(0, 0))==math.sqrt(20**2+20**2)
assert Point(-20, -20).distance_to_point(Point(0, 0))==math.sqrt(20**2+20**2)
assert Point(0, 0).distance_to_point(Point(-20, -20))==math.sqrt(20**2+20**2)

# --- Area of triangle
assert triangle_area_at_points(Point(0, 0), Point(0, 0), Point(0, 0))==0
assert round(triangle_area_at_points(Point(0, 0), Point(1, 1), Point(1, 0)), 2)==round(0.5, 2)
assert round(triangle_area_at_points(Point(0, 0), Point(1, 2), Point(1, 0)), 2)==round(1, 2)

# --- Point faces edge
edge = (Point(0, 0), Point(1, 1))
assert point_faces_edge(edge, Point(0, 2))
assert point_faces_edge(edge, Point(-1, 1))
assert point_faces_edge(edge, Point(0, 1))
assert point_faces_edge(edge, Point(1, -1))
assert point_faces_edge(edge, Point(5, -5))
assert not point_faces_edge(edge, Point(5, -7))
assert not point_faces_edge(edge, Point(0, 3))
edge = (Point(-5, -10), Point(-6, -11))
assert point_faces_edge(edge, Point(-5, -10))
assert point_faces_edge(edge, Point(-6, -11))
assert point_faces_edge(edge, Point(-6, -10))
assert not point_faces_edge(edge, Point(0, 0))
edge = (Point(-5, -100), Point(-5, 100))
assert point_faces_edge(edge, Point(-100, 0))
assert point_faces_edge(edge, Point(-100, 100))
assert not point_faces_edge(edge, Point(-100, 101))

# --- Distance between edge and point
edge = (Point(0, 0), Point(1, 1))
assert round(distance_between_edge_and_point(edge, Point(0, 1)), 2)==0.71
assert round(distance_between_edge_and_point(edge, Point(0, 2)), 2)==1.41
assert distance_between_edge_and_point(edge, Point(0, 0))==0
edge = (Point(0, 1), Point(2, 6)) # slope = 2, offset = (y=1)
assert distance_between_edge_and_point(edge, Point(0, 1))==0
assert distance_between_edge_and_point(edge, Point(2, 6))==0
edge = (Point(0, 0), Point(1, 2))  # slope = 2, offset = 0
assert round(distance_between_edge_and_point(edge, Point(0, 2)), 2)==0.89
edge = (Point(0.5, 0.5), Point(2.5, 0.5))
assert round(distance_between_edge_and_point(edge, Point(0, 1)), 2)==0.71
assert round(distance_between_edge_and_point(edge, Point(0, 0)), 2)==0.71
assert round(distance_between_edge_and_point(edge, Point(1, 1)), 2)==0.5
assert round(distance_between_edge_and_point(edge, Point(1, 0)), 2)==0.5

# -------------------------- Test properties ---------------------------

# Positive numbers
r1=Rect(100, 100, 30, 20)
assert r1.l_top  == Point(100.0, 100.0)
assert r1.r_top  == Point(130.0, 100.0)
assert r1.l_bot  == Point(100.0, 120.0)
assert r1.r_bot  == Point(130.0, 120.0)
assert r1.center == Point(100+30/2, 100+20/2)
assert r1.width  == 30.0
assert r1.height == 20.0

assert r1.is_point_inside_rect(Point(100, 100))
assert r1.is_point_inside_rect(Point(130, 100))
assert r1.is_point_inside_rect(Point(130, 120))
assert r1.is_point_inside_rect(Point(100, 120))
assert not r1.is_point_inside_rect(Point(131, 100))


# ---------------- Test relations with other rectangles ----------------

# --- Alignment
r1=Rect(0, 0, 50, 50)
r2=Rect(40, 40, 20, 20)
r1.align_with_top_edge_of(r2)
assert r1.l_top.y==r2.l_top.y
assert r1.r_top.y==r2.r_top.y
assert r1.l_bot.y==r1.l_top.y+r1.height
assert r1.r_bot.y==r1.l_top.y+r1.height
r1=Rect(0, 0, 50, 50)
r2=Rect(40, 40, 20, 20)
r1.align_with_left_edge_of(r2)
assert r1.l_top.x==r2.l_top.x
assert r1.l_bot.x==r2.l_bot.x
assert r1.r_bot.x==r1.l_top.x+r1.width
assert r1.r_top.x==r1.l_top.x+r1.width

# --- Overlapping
r1=Rect(100, 100, 30, 20)
r2=Rect(110, 100, 30, 20) # a bit to the right compared to r1
r3=Rect(100, 110, 30, 20) # a bit to the bottom compared to r1
r4=Rect(150, 150, 50, 50) # doesn't overlap at all
assert r1.overlaps_with(r2)
assert r1.overlaps_with(r3)
assert not r1.overlaps_with(r4)

# --- on x axis
r1=Rect(0,   0, 50, 50)
r2=Rect(0,  10, 50, 50)
r3=Rect(0, 500, 50, 50)
r4=Rect(500, 0, 50, 50)
assert r1.overlaps_on_x_axis_with(r2)
assert r1.overlaps_on_x_axis_with(r3)
assert not r1.overlaps_on_x_axis_with(r4)

# --- y axis
r1=Rect(0,     0, 50, 50)
r2=Rect(10,    0, 50, 50)
r3=Rect(50,    0, 50, 50)
r4=Rect(100,   0, 50, 50)
r5=Rect(  0, 100, 50, 50)
assert r1.overlaps_on_y_axis_with(r2)
assert r1.overlaps_on_y_axis_with(r3)
assert r1.overlaps_on_y_axis_with(r4)
assert not r1.overlaps_on_y_axis_with(r5)


# --- Distance between rectangles
w, h = 1, 1

# positives
r1=Rect( 0, 0, w, h)
r2=Rect( 1, 0, w, h)
r3=Rect( 2, 0, w, h)
r4=Rect( 0, 1, w, h)
r5=Rect( 1, 1, w, h)
r6=Rect( 2, 1, w, h)
r7=Rect( 0, 2, w, h)
r8=Rect( 1, 2, w, h)
r9=Rect( 2, 2, w, h)
r0=Rect( 0.5, 0.5, w, h)
assert r1.distance_to_rect(r2)==0.0
assert r1.distance_to_rect(r3)==1.0
assert r1.distance_to_rect(r4)==0.0
assert r1.distance_to_rect(r5)==0.0
assert r1.distance_to_rect(r6)==1.0
assert r1.distance_to_rect(r7)==1.0
assert r1.distance_to_rect(r8)==1.0
assert round(r1.distance_to_rect(r9), 2)==1.41
assert r1.distance_to_rect(r0)==0

#negative x
r1=Rect( 0, 0, w, h)
r2=Rect(-1, 0, w, h)
r3=Rect(-2, 0, w, h)
r4=Rect( 0, 1, w, h)
r5=Rect(-1, 1, w, h)
r6=Rect(-2, 1, w, h)
r7=Rect( 0, 2, w, h)
r8=Rect(-1, 2, w, h)
r9=Rect(-2, 2, w, h)
r0=Rect(-0.5, 0.5, w, h)
assert r1.distance_to_rect(r2)==0.0
assert r1.distance_to_rect(r3)==1.0
assert r1.distance_to_rect(r4)==0.0
assert r1.distance_to_rect(r5)==0.0
assert r1.distance_to_rect(r6)==1.0
assert r1.distance_to_rect(r7)==1.0
assert r1.distance_to_rect(r8)==1.0
assert round(r1.distance_to_rect(r9), 2)==1.41
assert r1.distance_to_rect(r0)==0

# negative y
r1=Rect( 0, 0, w, h)
r2=Rect( 1, 0, w, h)
r3=Rect( 2, 0, w, h)
r4=Rect( 0,-1, w, h)
r5=Rect( 1,-1, w, h)
r6=Rect( 2,-1, w, h)
r7=Rect( 0,-2, w, h)
r8=Rect( 1,-2, w, h)
r9=Rect( 2,-2, w, h)
r0=Rect( 0.5,-0.5, w, h)
assert r1.distance_to_rect(r2)==0.0
assert r1.distance_to_rect(r3)==1.0
assert r1.distance_to_rect(r4)==0.0
assert r1.distance_to_rect(r5)==0.0
assert r1.distance_to_rect(r6)==1.0
assert r1.distance_to_rect(r7)==1.0
assert r1.distance_to_rect(r8)==1.0
assert round(r1.distance_to_rect(r9), 2)==1.41
assert r1.distance_to_rect(r0)==0

#negative x and y
r1=Rect( 0, 0, w, h)
r2=Rect(-1, 0, w, h)
r3=Rect(-2, 0, w, h)
r4=Rect( 0,-1, w, h)
r5=Rect(-1,-1, w, h)
r6=Rect(-2,-1, w, h)
r7=Rect( 0,-2, w, h)
r8=Rect(-1,-2, w, h)
r9=Rect(-2,-2, w, h)
r0=Rect(-0.5,-0.5, w, h)
assert r1.distance_to_rect(r2)==0.0
assert r1.distance_to_rect(r3)==1.0
assert r1.distance_to_rect(r4)==0.0
assert r1.distance_to_rect(r5)==0.0
assert r1.distance_to_rect(r6)==1.0
assert r1.distance_to_rect(r7)==1.0
assert r1.distance_to_rect(r8)==1.0
assert round(r1.distance_to_rect(r9), 2)==1.41
assert r1.distance_to_rect(r0)==0


# overlap
r1=Rect(  0,   0, 50, 50)
r2=Rect( 10,  10, 50, 50)
assert r1.distance_to_rect(r2)==0
# overlap on x axis
r1=Rect(  0,   0, 50, 50)           # __
r2=Rect(  0,  60, 50, 50)           # __
assert round(r1.distance_to_rect(r2), 2)==10
r1=Rect(  0,   0, 50, 50)           # __
r2=Rect( 10,  60, 50, 50)           #  __
assert round(r1.distance_to_rect(r2), 2)==10
r1=Rect( 10,  60, 50, 50)           #  __
r2=Rect(  0,   0, 50, 50)           # __
assert round(r1.distance_to_rect(r2), 2)==10

# overlap on y axis
r1=Rect(  0,   0, 50, 50)           # ||
r2=Rect( 60,   0, 50, 50)
assert round(r1.distance_to_rect(r2), 2)==10
r1=Rect(  0,   0, 50, 50)           # |.
r2=Rect( 60,  10, 50, 50)           #  '
assert round(r1.distance_to_rect(r2), 2)==10
r1=Rect(  0,  20, 50, 50)           #  .
r2=Rect( 60,   0, 50, 50)           # |'
assert round(r1.distance_to_rect(r2), 2)==10

# ----------------------------------------------------------------------

print("No errors")
