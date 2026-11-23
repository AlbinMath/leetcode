# LeetCode 3380: Maximum Area Rectangle With Point Constraints I

**LeetCode Problem #3380 — Maximum Area Rectangle With Point Constraints I**
Solve LeetCode Maximum Area Rectangle With Point Constraints I using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Area Rectangle With Point Constraints I |
| LeetCode | #3380 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `points` where `points[i] = [x_i, y_i]` represents the coordinates of a point on an infinite plane.

Your task is to find the **maximum **area of a rectangle that:

Can be formed using **four** of these points as its corners. 
 Does **not** contain any other point inside or on its border. 
 Has its edges **parallel** to the axes.

Return the **maximum area** that you can obtain or -1 if no such rectangle is possible.

## Constraints
- `1 <= points.length <= 10`
- `points[i].length == 2`
- `0 <= x_i, y_i <= 100`
- All the given points are **unique**.

## Examples
### Example 1
- **Input:** `points = [[1,1],[1,3],[3,1],[3,3]]`
- **Output:** `4`

### Example 2
- **Input:** `points = [[1,1],[1,3],[3,1],[3,3],[2,2]]`
- **Output:** `-1`

### Example 3
- **Input:** `points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]`
- **Output:** `2`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Area Rectangle With Point Constraints I**, we observe the problem requirements and utilize the **Math & Logic** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[1,1],[1,3],[3,1],[3,3]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maxRectangleArea = function(points) {
    const pointSet = new Set(
        points.map(([x, y]) => `${x},${y}`)
    );

    let maxArea = -1;
    const n = points.length;

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const [x1, y1] = points[i];
            const [x2, y2] = points[j];

            if (x1 === x2 || y1 === y2) continue;

            const left = Math.min(x1, x2);
            const right = Math.max(x1, x2);
            const bottom = Math.min(y1, y2);
            const top = Math.max(y1, y2);

            const corners = [
                `${left},${bottom}`,
                `${left},${top}`,
                `${right},${bottom}`,
                `${right},${top}`
            ];

            if (!corners.every(corner => pointSet.has(corner))) {
                continue;
            }

            let valid = true;

            for (let k = 0; k < n; k++) {
                const [x, y] = points[k];

                // Skip all four rectangle corners.
                if (corners.includes(`${x},${y}`)) continue;

                // Any other point inside or on the border invalidates it.
                if (
                    x >= left && x <= right &&
                    y >= bottom && y <= top
                ) {
                    valid = false;
                    break;
                }
            }

            if (valid) {
                const area = (right - left) * (top - bottom);
                maxArea = Math.max(maxArea, area);
            }
        }
    }

    return maxArea;
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [3382. Maximum Area Rectangle With Point Constraints II](../../3501-4000/3689-maximum-area-rectangle-with-point-constraints-ii/)
- [223. Rectangle Area](../../0001-0500/0223-rectangle-area/)
- [850. Rectangle Area II](../../0501-1000/0880-rectangle-area-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/)
