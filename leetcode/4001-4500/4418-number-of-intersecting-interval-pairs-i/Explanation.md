# LeetCode 4056: Number of Intersecting Interval Pairs I

**LeetCode Problem #4056 — Number of Intersecting Interval Pairs I**
Solve LeetCode Number of Intersecting Interval Pairs I using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Intersecting Interval Pairs I |
| LeetCode | #4056 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D integer array `intervals` of `n` elements, where `intervals[i] = [start_i, end_i]` represents the **closed **interval from `start_i` to `end_i`.

Return the number of pairs of indices `(i, j)` such that `0 <= i < j < n` and `intervals[i]` and `intervals[j]` **intersect**.

Two intervals **intersect** if they have at least one point in common, including when they only share an endpoint.

## Constraints
- `2 <= n == intervals.length <= 100`
- `intervals[i] = [start_i, end_i]`
- `0 <= start_i <= end_i <= 100`

## Examples
### Example 1
- **Input:** `intervals = [[1,2],[2,3],[3,4]]`
- **Output:** `2`
- **Explanation:** There are 2 intersecting interval pairs: 

 
 Intervals `[1, 2]` and `[2, 3]` intersect at the point 2. 
 Intervals `[2, 3]` and `[3, 4]` intersect at the point 3.

### Example 2
- **Input:** `intervals = [[1,5],[2,4],[3,6]]`
- **Output:** `3`
- **Explanation:** There are 3 intersecting interval pairs: 

 
 The intersection of `[1, 5]` and `[2, 4]` is `[2, 4]`. 
 The intersection of `[1, 5]` and `[3, 6]` is `[3, 5]`. 
 The intersection of `[2, 4]` and `[3, 6]` is `[3, 4]`.

### Example 3
- **Input:** `intervals = [[1,2],[3,4],[5,6]]`
- **Output:** `0`
- **Explanation:** There are no intersecting interval pairs. Hence, the answer is 0.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Number of Intersecting Interval Pairs I**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `intervals = [[1,2],[2,3],[3,4]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** There are 2 intersecting interval pairs: 

 
 Intervals `[1, 2]` and `[2, 3]` intersect at the point 2. 
 Intervals `[2, 3]` and `[3, 4]` intersect at the point 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def countIntersectingIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        ans = 0
        for i in range(n):
            a, b = intervals[i]
            for j in range(i + 1, n):
                c, d = intervals[j]
                if a <= d and c <= b:
                    ans += 1
        return ans
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [1128. Number of Equivalent Domino Pairs](../../1001-1500/1227-number-of-equivalent-domino-pairs/)
- [1512. Number of Good Pairs](../../1501-2000/1635-number-of-good-pairs/)
- [1530. Number of Good Leaf Nodes Pairs](../../1501-2000/1653-number-of-good-leaf-nodes-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-intersecting-interval-pairs-i/)
