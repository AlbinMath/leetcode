# LeetCode 836: Rectangle Overlap

**LeetCode Problem #836 — Rectangle Overlap**
Solve LeetCode Rectangle Overlap using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rectangle Overlap |
| LeetCode | #836 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
An axis-aligned rectangle is represented as a list `[x1, y1, x2, y2]`, where `(x1, y1)` is the coordinate of its bottom-left corner, and `(x2, y2)` is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is **positive**. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles `rec1` and `rec2`, return `true`* if they overlap, otherwise return *`false`.

## Constraints
- `rec1.length == 4`
- `rec2.length == 4`
- `-10^9 <= rec1[i], rec2[i] <= 10^9`
- `rec1` and `rec2` represent a valid rectangle with a non-zero area.

## Examples
### Example 1
- **Input:** `rec1 = [0,0,2,2], rec2 = [1,1,3,3]`
- **Output:** `true`
- **Explanation:** The rectangles overlap in the region with corners at `(1,1)`, `(2,1)`, `(1,2)`, and `(2,2)`. 

 This region has positive area, so the rectangles overlap.

### Example 2
- **Input:** `rec1 = [0,0,1,1], rec2 = [1,0,2,1]`
- **Output:** `false`
- **Explanation:** The rectangles share the vertical edge where `x = 1`, but they do not have any common interior region. 

 Since their intersection has zero area, the rectangles do not overlap.

### Example 3
- **Input:** `rec1 = [0,0,1,1], rec2 = [2,2,3,3]`
- **Output:** `false`
- **Explanation:** The rectangles are completely separate. Rectangle `rec1` ends at `x = 1` and `y = 1`, while `rec2` starts at `x = 2` and `y = 2`. 

 Therefore, they have no common points and do not overlap.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code checks for overlap by verifying that neither rectangle is entirely to the left, right, above, or below the other. This is equivalent to checking that the intervals overlap in both dimensions:

- `rec1[0] < rec2[2]`: rec1's left edge is to the left of rec2's right edge.
- `rec2[0] < rec1[2]`: rec2's left edge is to the left of rec1's right edge.
- `rec1[1] < rec2[3]`: rec1's bottom edge is below rec2's top edge.
- `rec2[1] < rec1[3]`: rec2's bottom edge is below rec1's top edge.

If all four conditions are true, the rectangles overlap. Time and space complexity are both $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Primitive Types**).
2. Process elements sequentially using **Mathematical Simulation & Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `rec1 = [0,0,2,2], rec2 = [1,1,3,3]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The rectangles overlap in the region with corners at `(1,1)`, `(2,1)`, `(1,2)`, and `(2,2)`. 

 This region has positive area, so the rectangles overlap.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[]} rec1
 * @param {number[]} rec2
 * @return {boolean}
 */
var isRectangleOverlap = function(rec1, rec2) {
    return (
        rec1[0] < rec2[2] &&
        rec2[0] < rec1[2] &&
        rec1[1] < rec2[3] &&
        rec2[1] < rec1[3]
    );
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [84. Largest Rectangle in Histogram](../../0001-0500/0084-largest-rectangle-in-histogram/)
- [85. Maximal Rectangle](../../0001-0500/0085-maximal-rectangle/)
- [223. Rectangle Area](../../0001-0500/0223-rectangle-area/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rectangle-overlap/)
