# LeetCode 787: Cheapest Flights Within K Stops

**LeetCode Problem #787 — Cheapest Flights Within K Stops**
Solve LeetCode Cheapest Flights Within K Stops using JavaScript and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Cheapest Flights Within K Stops |
| LeetCode | #787 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [from_i, to_i, price_i]` indicates that there is a flight from city `from_i` to city `to_i` with cost `price_i`.

You are also given three integers `src`, `dst`, and `k`, return ***the cheapest price** from *`src`* to *`dst`* with at most *`k`* stops. *If there is no such route, return* *`-1`.

## Constraints
- `2 <= n <= 100`
- `0 <= flights.length <= (n * (n - 1) / 2)`
- `flights[i].length == 3`
- `0 <= from_i, to_i < n`
- `from_i != to_i`
- `1 <= price_i <= 10^4`
- There will not be any multiple flights between two cities.
- `0 <= src, dst, k < n`
- `src != dst`

## Examples
### Example 1
- **Input:** `n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1`
- **Output:** `700`
- **Explanation:** The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

### Example 2
- **Input:** `n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1`
- **Output:** `200`
- **Explanation:** The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

### Example 3
- **Input:** `n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0`
- **Output:** `500`
- **Explanation:** The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Cheapest Flights Within K Stops**, we observe the problem requirements and utilize the **Heap** technique. We iterate through the inputs using **Min/Max Heap Priority Selection**, leveraging a **Heap / Priority Queue** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Heap / Priority Queue**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `700`.
4. **Verification:** The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Heap / Priority Queue.

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var findCheapestPrice = function (n, flights, src, dst, k) {
    let dist = new Array(n).fill(Infinity);
    dist[src] = 0;

    for (let i = 0; i <= k; i++) {
        const next = dist.slice();
        for (const [u, v, w] of flights) {
            if (dist[u] !== Infinity && dist[u] + w < next[v]) {
                next[v] = dist[u] + w;
            }
        }
        dist = next;
    }

    return dist[dst] === Infinity ? -1 : dist[dst];
};
```

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2146. K Highest Ranked Items Within a Price Range](../../2001-2500/2250-k-highest-ranked-items-within-a-price-range/)
- [3505. Minimum Operations to Make Elements Within K Subarrays Equal](../../3501-4000/3717-minimum-operations-to-make-elements-within-k-subarrays-equal/)
- [1208. Get Equal Substrings Within Budget](../../1001-1500/1321-get-equal-substrings-within-budget/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
