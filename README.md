Python rectangles
=================

Generic rectangles in screen coordinates. Various methods are given to find if rectangles overlap, the distance between them, etc.

* A rectangle is made out of four points.
* Iterating over a rectangle iterates over its corner points.
* Screen coordinates are used (x grows from left to right, y grows from top to bottom). You can still use negative numbers.
* Works with both Python2 and Python3


Example
=================

    rect1=Rect( 0,  0, 10, 10)
    rect2=Rect(80, 50, 10, 10)
    print(rect1.distance_to_rect(rect2))



Interface
=================

is_point_inside_rect()

     ______
    |    . |
    |______|
    
* Takes: a `Point` instance
* Gives: `True` or `False`
         
------------------------------------------------------------------------

overlaps_with()

     ______
    |     _|____ 
    |____|      |
         |______|

* Takes: a `Rect` instance
* Gives: `True` or `False`
         
------------------------------------------------------------------------

overlaps_on_x_axis_with()

     ______
    |      |           
    |______|           Sees if the rectangles touch each other
        ______         if they were to be smashed to the top of
       |      |        the sreen.
       |______|

* Takes: a `Rect` instance
* Gives: `True` or `False`
         
------------------------------------------------------------------------

overlaps_on_y_axis_with()

     ______
    |      |   ______  Sees if the rectangles touch each other
    |______|  |      | if they were to be smashed to the left 
              |______| of the screen.

* Takes: a `Rect` instance
* Gives: `True` or `False`
         
------------------------------------------------------------------------

distance_to_rect()

     ______
    |      |             Finds the shortest distance between
    |______|             two rectangles. Both edges and corners
            \            are being taken into concideration.
             \ ______    
              |      |
              |______|

* Takes: a `Rect` instance
* Gives: distance in float
              

Rect
=================

A rectangle is the primary shape of this module. A rectangle is made out of four points (class Point is explained below). Iterating over a rectangle results into an iteration over its corners which essentially are points.

| Property 	| Description         	| Type  	|
|----------	|---------------------	|-------	|
| l_top    	| Left top corner     	| Point 	|
| r_top    	| Right top corner    	| Point 	|
| l_bot    	| Left bottom corner  	| Point 	|
| r_bot    	| Right bottom corner 	| Point 	|
| center   	| Center of rectangle 	| Point 	|
| width    	| Width of rectangle  	| Float 	|
| height   	| Height of rectangle  	| Float 	|

| Method                    	| Description                                                                                               	| Takes        	| Gives         	|
|---------------------------	|-----------------------------------------------------------------------------------------------------------	|--------------	|---------------	|
| copy()                    	| Gives a new copy of a rectangle                                                                           	| None         	| Rect          	|
| corners_belong_to_edge()  	| Tells if two points are the corners on the edge of the rectangle                                          	| Point, Point 	| True or False 	|
| is_point_inside_rect()    	| Tells if a point is inside the rectangle                                                                  	| Point        	| True or False 	|
| overlaps_with()           	| Tells if the rectangle overlaps with an other rectangle                                                   	| Rect         	| True or False 	|
| align_with_top_edge_of()  	| Moves rectangle to the top edge of given rectangle                                                        	| Rect         	| self          	|
| align_with_left_edge_of() 	| Moves rectangle to the left edge of given rectangle                                                       	| Rect         	| self          	|
| overlaps_on_x_axis_with() 	| Tells if the rectangle overlaps with an other rectangle if they were both moved to the top of the screen  	| Rect         	| True or False 	|
| overlaps_on_y_axis_with() 	| Tells if the rectangle overlaps with an other rectangle if they were both moved to the left of the screen 	| Rect         	| True or False 	|
| distance_to_rect()        	| Gives the shortest distance between two rectangles                                                        	| Rect         	| Float         	|


Point
=================

Since rectangle is made out of four points it's reasonable that you will want to know a bit about the class Point.
Also keep in mind that some methods of a rectangle take points as an argument.

| Property 	| Description           	| Type  	|
|----------	|-----------------------	|-------	|
| x        	| Coordinates on x axis 	| Float 	|
| y        	| Coordinates on y axis 	| Point 	|


| Method                    	| Description                                                                                               	| Takes          	| Gives         	|
|---------------------------	|-----------------------------------------------------------------------------------------------------------	|----------------	|---------------	|
| distance_to_point()       	| Gives the distance to a point                                                                             	| Point          	| Float         	|
| faces_line()              	| Tells if point is facing a line (a tupple of two points)                                                  	| (Point, Point) 	| True or False 	|
