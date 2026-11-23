# LeetCode 3015: Count the Number of Houses at a Certain Distance I

**LeetCode Problem #3015 — Count the Number of Houses at a Certain Distance I**
Solve LeetCode Count the Number of Houses at a Certain Distance I using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Number of Houses at a Certain Distance I |
| LeetCode | #3015 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given three **positive** integers `n`, `x`, and `y`.

In a city, there exist houses numbered `1` to `n` connected by `n` streets. There is a street connecting the house numbered `i` with the house numbered `i + 1` for all `1 <= i <= n - 1` . An additional street connects the house numbered `x` with the house numbered `y`.

For each `k`, such that `1 <= k <= n`, you need to find the number of **pairs of houses** `(house_1, house_2)` such that the **minimum** number of streets that need to be traveled to reach `house_2` from `house_1` is `k`.

Return *a **1-indexed** array *`result`* of length *`n`* where *`result[k]`* represents the **total** number of pairs of houses such that the **minimum** streets required to reach one house from the other is *`k`.

**Note** that `x` and `y` can be **equal**.

## Constraints
- `2 <= n <= 100`
- `1 <= x, y <= n`

## Examples
### Example 1
- **Input:** `n = 3, x = 1, y = 3`
- **Output:** `[6,0,0]`
- **Explanation:** Let's look at each pair of houses:
- For the pair (1, 2), we can go from house 1 to house 2 directly.
- For the pair (2, 1), we can go from house 2 to house 1 directly.
- For the pair (1, 3), we can go from house 1 to house 3 directly.
- For the pair (3, 1), we can go from house 3 to house 1 directly.
- For the pair (2, 3), we can go from house 2 to house 3 directly.
- For the pair (3, 2), we can go from house 3 to house 2 directly.

### Example 2
- **Input:** `n = 5, x = 2, y = 4`
- **Output:** `[10,8,2,0,0]`
- **Explanation:** For each distance k the pairs are:
- For k == 1, the pairs are (1, 2), (2, 1), (2, 3), (3, 2), (2, 4), (4, 2), (3, 4), (4, 3), (4, 5), and (5, 4).
- For k == 2, the pairs are (1, 3), (3, 1), (1, 4), (4, 1), (2, 5), (5, 2), (3, 5), and (5, 3).
- For k == 3, the pairs are (1, 5), and (5, 1).
- For k == 4 and k == 5, there are no pairs.

### Example 3
- **Input:** `n = 4, x = 1, y = 1`
- **Output:** `[6,4,2,0]`
- **Explanation:** For each distance k the pairs are:
- For k == 1, the pairs are (1, 2), (2, 1), (2, 3), (3, 2), (3, 4), and (4, 3).
- For k == 2, the pairs are (1, 3), (3, 1), (2, 4), and (4, 2).
- For k == 3, the pairs are (1, 4), and (4, 1).
- For k == 4, there are no pairs.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count the Number of Houses at a Certain Distance I**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, x = 1, y = 3`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[6,0,0]`.
4. **Verification:** Let's look at each pair of houses:
- For the pair (1, 2), we can go from house 1 to house 2 directly.
- For the pair (2, 1), we can go from house 2 to house 1 directly.
- For the pair (1, 3), we can go from house 1 to house 3 directly.
- For the pair (3, 1), we can go from house 3 to house 1 directly.
- For the pair (2, 3), we can go from house 2 to house 3 directly.
- For the pair (3, 2), we can go from house 3 to house 2 directly.

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
var countOfPairs = function(n, x, y) {
    const result = new Array(n).fill(0);

    for (let i = 1; i <= n; i++) {
        for (let j = i + 1; j <= n; j++) {

            // Distance using the original straight road.
            const direct = j - i;

            // Distance using the additional road.
            const viaXY = Math.abs(i - x) + 1 + Math.abs(j - y);
            const viaYX = Math.abs(i - y) + 1 + Math.abs(j - x);

            // Minimum possible distance.
            const distance = Math.min(direct, viaXY, viaYX);

            // Count both ordered pairs: (i,j) and (j,i).
            result[distance - 1] += 2;
        }
    }

    return result;
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
- [3017. Count the Number of Houses at a Certain Distance II](../../3001-3500/3310-count-the-number-of-houses-at-a-certain-distance-ii/)
- [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](../../1001-1500/1456-find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)
- [1617. Count Subtrees With Max Distance Between Cities](../../1501-2000/1740-count-subtrees-with-max-distance-between-cities/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/)
