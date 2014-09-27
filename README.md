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



Rectangle methods
=================

     ______
    |    . |
    |______|
    

    point=Point(40, 40)
    rect1.is_point_inside_rect(point)
    
Takes: a Point instance
Gives: True or False
         
------------------------------------------------------------------------

overlaps_with()

     ______
    |     _|____ 
    |____|      |
         |______|

Takes: a Rect instance
Gives: True or False
         
------------------------------------------------------------------------

overlaps_on_x_axis_with()

     ______
    |      |           
    |______|           Sees if the rectangles touch each other
        ______         if they were to be smashed to the top of
       |      |        the sreen.
       |______|

Takes: a Rect instance
Gives: True or False
         
------------------------------------------------------------------------

overlaps_on_y_axis_with()

     ______
    |      |   ______  Sees if the rectangles touch each other
    |______|  |      | if they were to be smashed to the left 
              |______| of the screen.

Takes: a Rect instance
Gives: True or False
         
------------------------------------------------------------------------

distance_to_rect()

	 ______
    |      |             Finds the shortest distance between
    |______|             two rectangles. Both edges and corners
            \            are being taken into concideration.
             \ ______    
              |      |
              |______|

Takes: a Rect instance	
Gives: distance in float
              
