# LeetCode 3244: Shortest Distance After Road Addition Queries II

**LeetCode Problem #3244 — Shortest Distance After Road Addition Queries II**
Solve LeetCode Shortest Distance After Road Addition Queries II using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Distance After Road Addition Queries II |
| LeetCode | #3244 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n` and a 2D integer array `queries`.

There are `n` cities numbered from `0` to `n - 1`. Initially, there is a **unidirectional** road from city `i` to city `i + 1` for all `0 <= i < n - 1`.

`queries[i] = [u_i, v_i]` represents the addition of a new **unidirectional** road from city `u_i` to city `v_i`. After each query, you need to find the **length** of the **shortest path** from city `0` to city `n - 1`.

There are no two queries such that `queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]`.

Return an array `answer` where for each `i` in the range `[0, queries.length - 1]`, `answer[i]` is the *length of the shortest path* from city `0` to city `n - 1` after processing the **first **`i + 1` queries.

## Constraints
- `3 <= n <= 10^5`
- `1 <= queries.length <= 10^5`
- `queries[i].length == 2`
- `0 <= queries[i][0] < queries[i][1] < n`
- `1 < queries[i][1] - queries[i][0]`
- There are no repeated roads among the queries.
- There are no two queries such that `i != j` and `queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]`.

## Examples
### Example 1
- **Input:** `n = 5, queries = [[2,4],[0,2],[0,4]]`
- **Output:** `[3,2,1]`
- **Explanation:** After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3. 

 

 After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2. 

 

 After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

### Example 2
- **Input:** `n = 4, queries = [[0,3],[0,2]]`
- **Output:** `[1,1]`
- **Explanation:** After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1. 

 

 After the addition of the road from 0 to 2, the length of the shortest path remains 1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Shortest Distance After Road Addition Queries II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, queries = [[2,4],[0,2],[0,4]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,2,1]`.
4. **Verification:** After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3. 

 

 After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2. 

 

 After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

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
var shortestDistanceAfterQueries = function(n, queries) {
    const next = new Array(n);

    for (let i = 0; i < n; i++) {
        next[i] = i + 1;
    }

    let distance = n - 1;
    const answer = [];

    for (const [u, v] of queries) {

        // Ignore the query if either endpoint was removed.
        if (next[u] === -1 || next[v] === -1) {
            answer.push(distance);
            continue;
        }

        // Remove all active cities between u and v.
        let city = next[u];

        while (city !== v) {
            const following = next[city];

            next[city] = -1;
            distance--;

            city = following;
        }

        // Connect u directly to v.
        next[u] = v;

        answer.push(distance);
    }

    return answer;
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
- [3243. Shortest Distance After Road Addition Queries I](../../3501-4000/3517-shortest-distance-after-road-addition-queries-i/)
- [821. Shortest Distance to a Character](../../0501-1000/0841-shortest-distance-to-a-character/)
- [985. Sum of Even Numbers After Queries](../../1001-1500/1027-sum-of-even-numbers-after-queries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/)
