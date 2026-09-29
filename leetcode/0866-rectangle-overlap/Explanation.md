# Rectangle Overlap

## Problem Explanation
A rectangle is represented as a list `[x1, y1, x2, y2]`, where `(x1, y1)` is the bottom-left corner and `(x2, y2)` is the top-right corner. Two rectangles overlap if they share a positive area. Return `true` if the two given rectangles overlap.

## How the Code Works
The code checks for overlap by verifying that neither rectangle is entirely to the left, right, above, or below the other. This is equivalent to checking that the intervals overlap in both dimensions:

- `rec1[0] < rec2[2]`: rec1's left edge is to the left of rec2's right edge.
- `rec2[0] < rec1[2]`: rec2's left edge is to the left of rec1's right edge.
- `rec1[1] < rec2[3]`: rec1's bottom edge is below rec2's top edge.
- `rec2[1] < rec1[3]`: rec2's bottom edge is below rec1's top edge.

If all four conditions are true, the rectangles overlap. Time and space complexity are both $O(1)$.
