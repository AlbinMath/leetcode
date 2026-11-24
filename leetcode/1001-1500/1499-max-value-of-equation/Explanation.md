# LeetCode 1499: Max Value of Equation

**LeetCode Problem #1499 — Max Value of Equation**
Solve LeetCode Max Value of Equation using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Max Value of Equation |
| LeetCode | #1499 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `points` containing the coordinates of points on a 2D plane, sorted by the x-values, where `points[i] = [x_i, y_i]` such that `x_i < x_j` for all `1 <= i < j <= points.length`. You are also given an integer `k`.

Return *the maximum value of the equation *`y_i + y_j + |x_i - x_j|` where `|x_i - x_j| <= k` and `1 <= i < j <= points.length`.

It is guaranteed that there exists at least one pair of points that satisfy the constraint `|x_i - x_j| <= k`.

## Constraints
- `2 <= points.length <= 10^5`
- `points[i].length == 2`
- `-10^8 <= x_i, y_i <= 10^8`
- `0 <= k <= 2 * 10^8`
- `x_i < x_j` for all `1 <= i < j <= points.length`
- `x_i` form a strictly increasing sequence.

## Examples
### Example 1
- **Input:** `points = [[1,3],[2,0],[5,10],[6,-10]], k = 1`
- **Output:** `4`
- **Explanation:** The first two points satisfy the condition |x_i - x_j| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.

### Example 2
- **Input:** `points = [[0,0],[3,0],[9,2]], k = 3`
- **Output:** `3`
- **Explanation:** Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Max Value of Equation**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[1,3],[2,0],[5,10],[6,-10]], k = 1`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The first two points satisfy the condition |x_i - x_j| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number}
 */
var findMaxValueOfEquation = function (points, k) {
    const n = points.length;
    const dq = new Array(n);
    let head = 0, tail = 0; // deque occupies dq[head..tail-1]
    let ans = -Infinity;

    for (let j = 0; j < n; j++) {
        const [xj, yj] = points[j];

        while (head < tail && xj - points[dq[head]][0] > k) head++;

        if (head < tail) {
            const [xi, yi] = points[dq[head]];
            ans = Math.max(ans, (yi - xi) + (yj + xj));
        }

        const val = yj - xj;
        while (head < tail) {
            const [xb, yb] = points[dq[tail - 1]];
            if (yb - xb <= val) tail--;
            else break;
        }
        dq[tail++] = j;
    }
    return ans;
};
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [513. Find Bottom Left Tree Value](../../0501-1000/0513-find-bottom-left-tree-value/)
- [515. Find Largest Value in Each Tree Row](../../0501-1000/0515-find-largest-value-in-each-tree-row/)
- [981. Time Based Key-Value Store](../../0501-1000/0981-time-based-key-value-store/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/max-value-of-equation/)
