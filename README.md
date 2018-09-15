# quick hull  
### jmiu CS4306  
Uses Python 3.6  

# REPORT  
## Original Assignment  
Implement the quick hull algorithm.  

## Solution  
I implemented the quick hull algorithm as described on [wikipedia](https://en.wikipedia.org/wiki/Quickhull), with a single modification. This modification was reversing the order of `FindHull(S1, P, C)` and `FindHull(S2, C, Q)` when running on the top half of the points. Without this inclusion, the algorithm was not reliably producing a convex hull on the top points.  

## Example Output  
Example output has been provided in the form of [plot.png](https://github.com/DariusMiu/quick-hull/blob/master/plot.png)  