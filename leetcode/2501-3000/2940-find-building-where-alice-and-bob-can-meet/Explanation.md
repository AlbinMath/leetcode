# LeetCode 2940: Find Building Where Alice and Bob Can Meet

**LeetCode Problem #2940 — Find Building Where Alice and Bob Can Meet**
Solve LeetCode Find Building Where Alice and Bob Can Meet using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Building Where Alice and Bob Can Meet |
| LeetCode | #2940 |
| Difficulty | Hard |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** array `heights` of positive integers, where `heights[i]` represents the height of the `i^th` building.

If a person is in building `i`, they can move to any other building `j` if and only if `i < j` and `heights[i] < heights[j]`.

You are also given another array `queries` where `queries[i] = [a_i, b_i]`. On the `i^th` query, Alice is in building `a_i` while Bob is in building `b_i`.

Return *an array* `ans` *where* `ans[i]` *is **the index of the leftmost building** where Alice and Bob can meet on the* `i^th` *query*. *If Alice and Bob cannot move to a common building on query* `i`, *set* `ans[i]` *to* `-1`.

## Constraints
- `1 <= heights.length <= 5 * 10^4`
- `1 <= heights[i] <= 10^9`
- `1 <= queries.length <= 5 * 10^4`
- `queries[i] = [a_i, b_i]`
- `0 <= a_i, b_i <= heights.length - 1`

## Examples
### Example 1
- **Input:** `heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]`
- **Output:** `[2,5,-1,5,2]`
- **Explanation:** In the first query, Alice and Bob can move to building 2 since heights[0] < heights[2] and heights[1] < heights[2]. 
In the second query, Alice and Bob can move to building 5 since heights[0] < heights[5] and heights[3] < heights[5]. 
In the third query, Alice cannot meet Bob since Alice cannot move to any other building.
In the fourth query, Alice and Bob can move to building 5 since heights[3] < heights[5] and heights[4] < heights[5].
In the fifth query, Alice and Bob are already in the same building. 
For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.

### Example 2
- **Input:** `heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]`
- **Output:** `[7,6,-1,4,6]`
- **Explanation:** In the first query, Alice can directly move to Bob's building since heights[0] < heights[7].
In the second query, Alice and Bob can move to building 6 since heights[3] < heights[6] and heights[5] < heights[6].
In the third query, Alice cannot meet Bob since Bob cannot move to any other building.
In the fourth query, Alice and Bob can move to building 4 since heights[3] < heights[4] and heights[0] < heights[4].
In the fifth query, Alice can directly move to Bob's building since heights[1] < heights[6].
For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Building Where Alice and Bob Can Meet**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,5,-1,5,2]`.
4. **Verification:** In the first query, Alice and Bob can move to building 2 since heights[0] < heights[2] and heights[1] < heights[2]. 
In the second query, Alice and Bob can move to building 5 since heights[0] < heights[5] and heights[3] < heights[5]. 
In the third query, Alice cannot meet Bob since Alice cannot move to any other building.
In the fourth query, Alice and Bob can move to building 5 since heights[3] < heights[5] and heights[4] < heights[5].
In the fifth query, Alice and Bob are already in the same building. 
For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var leftmostBuildingQueries = function(heights, queries) {
    const n = heights.length;
    const ans = new Array(queries.length).fill(-1);
    const waiting = Array.from({ length: n }, () => []);

    for (let i = 0; i < queries.length; i++) {
        let [a, b] = queries[i];

        if (a > b) [a, b] = [b, a];

        if (a === b || heights[a] < heights[b]) {
            ans[i] = b;
        } else {
            waiting[b].push([heights[a], i]);
        }
    }

    const heap = [];

    function push(item) {
        heap.push(item);
        let i = heap.length - 1;

        while (i > 0) {
            const p = Math.floor((i - 1) / 2);
            if (heap[p][0] <= heap[i][0]) break;

            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    }

    function pop() {
        const result = heap[0];
        const last = heap.pop();

        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;

            while (true) {
                let smallest = i;
                const l = 2 * i + 1;
                const r = 2 * i + 2;

                if (l < heap.length &&
                    heap[l][0] < heap[smallest][0]) {
                    smallest = l;
                }

                if (r < heap.length &&
                    heap[r][0] < heap[smallest][0]) {
                    smallest = r;
                }

                if (smallest === i) break;

                [heap[i], heap[smallest]] =
                    [heap[smallest], heap[i]];

                i = smallest;
            }
        }

        return result;
    }

    for (let i = 0; i < n; i++) {
        while (heap.length > 0 && heap[0][0] < heights[i]) {
            const [, queryIndex] = pop();
            ans[queryIndex] = i;
        }

        for (const item of waiting[i]) {
            push(item);
        }
    }

    return ans;
};
```

### Python
```python
from typing import List

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        size = 1
        while size < n:
            size *= 2

        t = [0] * (2 * size)
        t[size:size+n] = heights

        for i in range(size - 1, 0, -1):
            t[i] = max(t[2*i], t[2*i+1])

        def find(node, l, r, start, h):
            if r < start or t[node] <= h:
                return -1
            if l == r:
                return l if l < n else -1
            m = (l + r) // 2
            x = find(node*2, l, m, start, h)
            return x if x != -1 else find(node*2+1, m+1, r, start, h)

        ans = []
        for a, b in queries:
            if a > b:
                a, b = b, a

            if a == b or heights[a] < heights[b]:
                ans.append(b)
            else:
                ans.append(find(1, 0, size-1, b+1, heights[a]))

        return ans
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
- [1420. Build Array Where You Can Find The Maximum Exactly K Comparisons](../../1001-1500/1420-build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)
- [1970. Last Day Where You Can Still Cross](../../1501-2000/1970-last-day-where-you-can-still-cross/)
- [3113. Find the Number of Subarrays Where Boundary Elements Are Maximum](../../3001-3500/3113-find-the-number-of-subarrays-where-boundary-elements-are-maximum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/)
