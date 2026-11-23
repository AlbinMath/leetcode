# LeetCode 3161: Block Placement Queries

**LeetCode Problem #3161 — Block Placement Queries**
Solve LeetCode Block Placement Queries using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Block Placement Queries |
| LeetCode | #3161 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There exists an infinite number line, with its origin at 0 and extending towards the **positive** x-axis.

You are given a 2D array `queries`, which contains two types of queries:

For a query of type 1, `queries[i] = [1, x]`. Build an obstacle at distance `x` from the origin. It is guaranteed that there is **no** obstacle at distance `x` when the query is asked. 
 For a query of type 2, `queries[i] = [2, x, sz]`. Check if it is possible to place a block of size `sz` *anywhere* in the range `[0, x]` on the line, such that the block **entirely** lies in the range `[0, x]`. A block **cannot **be placed if it intersects with any obstacle, but it may touch it. Note that you do** not** actually place the block. Queries are separate.

Return a boolean array `results`, where `results[i]` is `true` if you can place the block specified in the `i^th` query of type 2, and `false` otherwise.

## Constraints
- `1 <= queries.length <= 15 * 10^4`
- `2 <= queries[i].length <= 3`
- `1 <= queries[i][0] <= 2`
- `1 <= x, sz <= min(5 * 10^4, 3 * queries.length)`
- The input is generated such that for queries of type 1, no obstacle exists at distance `x` when the query is asked.
- The input is generated such that there is at least one query of type 2.

## Examples
### Example 1
- **Input:** `queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]`
- **Output:** `[false,true,true]`

### Example 2
- **Input:** `queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]`
- **Output:** `[true,true,false]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Block Placement Queries**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[false,true,true]`.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:

    def getResults(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[bool]
        """

        # Maximum coordinate that can appear.
        max_x = 0

        for q in queries:
            max_x = max(max_x, q[1])

        size = 4 * (max_x + 2)

        # Segment tree arrays.
        #
        # first[node] = first obstacle in this segment
        # last[node]  = last obstacle in this segment
        # gap[node]   = maximum gap between obstacles
        #
        # -1 means there is no obstacle.
        first = [-1] * size
        last = [-1] * size
        gap = [0] * size

        def pull(node):
            left = node * 2
            right = left + 1

            # Only left child has obstacles
            if first[right] == -1:
                first[node] = first[left]
                last[node] = last[left]
                gap[node] = gap[left]
                return

            # Only right child has obstacles
            if first[left] == -1:
                first[node] = first[right]
                last[node] = last[right]
                gap[node] = gap[right]
                return

            # Both sides contain obstacles.
            first[node] = first[left]
            last[node] = last[right]

            gap[node] = max(
                gap[left],
                gap[right],
                first[right] - last[left]
            )

        def update(node, lo, hi, pos):
            if lo == hi:
                first[node] = pos
                last[node] = pos
                gap[node] = 0
                return

            mid = (lo + hi) // 2

            if pos <= mid:
                update(node * 2, lo, mid, pos)
            else:
                update(node * 2 + 1, mid + 1, hi, pos)

            pull(node)

        def query(node, lo, hi, ql, qr):
            # No overlap
            if qr < lo or hi < ql:
                return (-1, -1, 0)

            # Complete overlap
            if ql <= lo and hi <= qr:
                return (
                    first[node],
                    last[node],
                    gap[node]
                )

            mid = (lo + hi) // 2

            lf, ll, lg = query(
                node * 2,
                lo,
                mid,
                ql,
                qr
            )

            rf, rl, rg = query(
                node * 2 + 1,
                mid + 1,
                hi,
                ql,
                qr
            )

            # Left empty
            if lf == -1:
                return (rf, rl, rg)

            # Right empty
            if rf == -1:
                return (lf, ll, lg)

            return (
                lf,
                rl,
                max(lg, rg, rf - ll)
            )

        answer = []

        for q in queries:

            # Type 1: add obstacle
            if q[0] == 1:
                x = q[1]
                update(1, 1, max_x, x)

            # Type 2: check block placement
            else:
                x = q[1]
                sz = q[2]

                # Obstacles only matter in [1, x].
                f, l, max_gap = query(
                    1,
                    1,
                    max_x,
                    1,
                    x
                )

                # No obstacle in [1, x].
                if f == -1:
                    answer.append(x >= sz)
                    continue

                # Gap from origin to first obstacle.
                max_gap = max(max_gap, f)

                # Gap from last obstacle to x.
                max_gap = max(max_gap, x - l)

                answer.append(max_gap >= sz)

        return answer
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
- [1314. Matrix Block Sum](../../1001-1500/1242-matrix-block-sum/)
- [4038. Count Integers Appearing in a Single Block](../../4001-4500/4410-count-integers-appearing-in-a-single-block/)
- [985. Sum of Even Numbers After Queries](../../1001-1500/1027-sum-of-even-numbers-after-queries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/block-placement-queries/)
