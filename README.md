Requirements:
- Python3
- Matlpotlib


INPUT:

The first line would specify polygon or disc based on what shape you want to input.

In case of polygon, the next line would consist of space separated x coordinates of all the vertices of the polygon, and the line after that will contain the corresponding y coordinates of the vertices.

In case of disc, the next line would consist of space separated x and y coordinates of the center and the radius of circle (x y r).

There are 3 kinds of transformations that can be applied to the shapes:
- Scaling: Input format: S x-scale y-scale
- Rotation: Input format: R angle
- Translation: Input format: T x-shift y-shift
  
  
  
OUTPUT:

The coordinates of the transformed shape after applying the transformation will be printed in the same format as the input, and the plot of the shape would be displayed on a matplotlib window.
