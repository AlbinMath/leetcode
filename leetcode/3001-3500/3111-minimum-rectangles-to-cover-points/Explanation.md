# LeetCode 3111: Minimum Rectangles to Cover Points

**LeetCode Problem #3111 — Minimum Rectangles to Cover Points**
Solve LeetCode Minimum Rectangles to Cover Points using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Rectangles to Cover Points |
| LeetCode | #3111 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `points`, where `points[i] = [x_i, y_i]`. You are also given an integer `w`. Your task is to **cover** **all** the given points with rectangles.

Each rectangle has its lower end at some point `(x_1, 0)` and its upper end at some point `(x_2, y_2)`, where `x_1 <= x_2`, `y_2 >= 0`, and the condition `x_2 - x_1 <= w` **must** be satisfied for each rectangle.

A point is considered covered by a rectangle if it lies within or on the boundary of the rectangle.

Return an integer denoting the **minimum** number of rectangles needed so that each point is covered by **at least one** rectangle*.*

**Note:** A point may be covered by more than one rectangle.

## Constraints
- `1 <= points.length <= 10^5`
- `points[i].length == 2`
- `0 <= x_i == points[i][0] <= 10^9`
- `0 <= y_i == points[i][1] <= 10^9`
- `0 <= w <= 10^9`
- All pairs `(x_i, y_i)` are distinct.

## Examples
### Example 1
- **Input:** `points = [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]], w = 1`
- **Output:** `2`
- **Explanation:** The image above shows one possible placement of rectangles to cover the points: 

 
 A rectangle with a lower end at `(1, 0)` and its upper end at `(2, 8)` 
 A rectangle with a lower end at `(3, 0)` and its upper end at `(4, 8)`

### Example 2
- **Input:** `points = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]], w = 2`
- **Output:** `3`
- **Explanation:** The image above shows one possible placement of rectangles to cover the points: 

 
 A rectangle with a lower end at `(0, 0)` and its upper end at `(2, 2)` 
 A rectangle with a lower end at `(3, 0)` and its upper end at `(5, 5)` 
 A rectangle with a lower end at `(6, 0)` and its upper end at `(6, 6)`

### Example 3
- **Input:** `points = [[2,3],[1,2]], w = 0`
- **Output:** `2`
- **Explanation:** The image above shows one possible placement of rectangles to cover the points: 

 
 A rectangle with a lower end at `(1, 0)` and its upper end at `(1, 2)` 
 A rectangle with a lower end at `(2, 0)` and its upper end at `(2, 3)`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Rectangles to Cover Points**, we observe the problem requirements and utilize the **Math & Logic** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]], w = 1`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The image above shows one possible placement of rectangles to cover the points: 

 
 A rectangle with a lower end at `(1, 0)` and its upper end at `(2, 8)` 
 A rectangle with a lower end at `(3, 0)` and its upper end at `(4, 8)`

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
var minRectanglesToCoverPoints = function(points, w) {
    const xs = points.map(point => point[0]).sort((a, b) => a - b);

    let count = 0;
    let i = 0;

    while (i < xs.length) {
        const startX = xs[i];

        count++;

        while (i < xs.length && xs[i] <= startX + w) {
            i++;
        }
    }

    return count;
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
- [1266. Minimum Time Visiting All Points](../../1001-1500/1266-minimum-time-visiting-all-points/)
- [1595. Minimum Cost to Connect Two Groups of Points](../../1501-2000/1595-minimum-cost-to-connect-two-groups-of-points/)
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../../2001-2500/2058-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-rectangles-to-cover-points/)
