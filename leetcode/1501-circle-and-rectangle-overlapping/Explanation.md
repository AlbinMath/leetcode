# Circle And Rectangle Overlapping

## Problem Explanation
Given a circle (center `(xCenter, yCenter)` and `radius`) and an axis-aligned rectangle (`x1, y1, x2, y2`), return whether they overlap.

## How the Code Works
The code finds the closest point on the rectangle to the circle's center and checks if it's within the radius. The closest point is found by clamping the center's coordinates to the rectangle's bounds. If the distance from the center to this closest point is ≤ radius, they overlap.

Time and space complexity are both $O(1)$.
