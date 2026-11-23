# LeetCode 2250: Count Number of Rectangles Containing Each Point

**LeetCode Problem #2250 — Count Number of Rectangles Containing Each Point**
Solve LeetCode Count Number of Rectangles Containing Each Point using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Number of Rectangles Containing Each Point |
| LeetCode | #2250 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `rectangles` where `rectangles[i] = [l_i, h_i]` indicates that `i^th` rectangle has a length of `l_i` and a height of `h_i`. You are also given a 2D integer array `points` where `points[j] = [x_j, y_j]` is a point with coordinates `(x_j, y_j)`.

The `i^th` rectangle has its **bottom-left corner** point at the coordinates `(0, 0)` and its **top-right corner** point at `(l_i, h_i)`.

Return* an integer array *`count`* of length *`points.length`* where *`count[j]`* is the number of rectangles that **contain** the *`j^th`* point.*

The `i^th` rectangle **contains** the `j^th` point if `0 <= x_j <= l_i` and `0 <= y_j <= h_i`. Note that points that lie on the **edges** of a rectangle are also considered to be contained by that rectangle.

## Constraints
- `1 <= rectangles.length, points.length <= 5 * 10^4`
- `rectangles[i].length == points[j].length == 2`
- `1 <= l_i, x_j <= 10^9`
- `1 <= h_i, y_j <= 100`
- All the `rectangles` are **unique**.
- All the `points` are **unique**.

## Examples
### Example 1
- **Input:** `rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]`
- **Output:** `[2,1]`
- **Explanation:** The first rectangle contains no points.
The second rectangle contains only the point (2, 1).
The third rectangle contains the points (2, 1) and (1, 4).
The number of rectangles that contain the point (2, 1) is 2.
The number of rectangles that contain the point (1, 4) is 1.
Therefore, we return [2, 1].

### Example 2
- **Input:** `rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]`
- **Output:** `[1,3]`
- **Explanation:** The first rectangle contains only the point (1, 1).
The second rectangle contains only the point (1, 1).
The third rectangle contains the points (1, 3) and (1, 1).
The number of rectangles that contain the point (1, 3) is 1.
The number of rectangles that contain the point (1, 1) is 3.
Therefore, we return [1, 3].

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Count Number of Rectangles Containing Each Point**, we observe the problem requirements and utilize the **Math & Logic** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,1]`.
4. **Verification:** The first rectangle contains no points.
The second rectangle contains only the point (2, 1).
The third rectangle contains the points (2, 1) and (1, 4).
The number of rectangles that contain the point (2, 1) is 2.
The number of rectangles that contain the point (1, 4) is 1.
Therefore, we return [2, 1].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var countRectangles = function(rectangles, points) {
    const heights = Array.from({ length: 101 }, () => []);

    // Group rectangle lengths by height
    for (const [l, h] of rectangles) {
        heights[h].push(l);
    }

    // Sort lengths for binary search
    for (let h = 1; h <= 100; h++) {
        heights[h].sort((a, b) => a - b);
    }

    function lowerBound(arr, target) {
        let left = 0;
        let right = arr.length;

        while (left < right) {
            const mid = Math.floor((left + right) / 2);

            if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }

    const result = [];

    for (const [x, y] of points) {
        let count = 0;

        // A containing rectangle must have height >= y
        for (let h = y; h <= 100; h++) {
            const arr = heights[h];
            const index = lowerBound(arr, x);

            // All lengths from index onward are >= x
            count += arr.length - index;
        }

        result.push(count);
    }

    return result;
};
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [1178. Number of Valid Words for Each Puzzle](../../1001-1500/1282-number-of-valid-words-for-each-puzzle/)
- [1434. Number of Ways to Wear Different Hats to Each Other](../../1501-2000/1531-number-of-ways-to-wear-different-hats-to-each-other/)
- [1731. The Number of Employees Which Report to Each Employee](../../1501-2000/1882-the-number-of-employees-which-report-to-each-employee/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/)
