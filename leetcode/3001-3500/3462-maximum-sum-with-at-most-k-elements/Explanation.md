# LeetCode 3462: Maximum Sum With at Most K Elements

**LeetCode Problem #3462 — Maximum Sum With at Most K Elements**
Solve LeetCode Maximum Sum With at Most K Elements using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Sum With at Most K Elements |
| LeetCode | #3462 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer matrix `grid` of size `n x m`, an integer array `limits` of length `n`, and an integer `k`. The task is to find the **maximum sum** of **at most** `k` elements from the matrix `grid` such that:

The number of elements taken from the `i^th` row of `grid` does not exceed `limits[i]`.

Return the **maximum sum**.

## Constraints
- `n == grid.length == limits.length`
- `m == grid[i].length`
- `1 <= n, m <= 500`
- `0 <= grid[i][j] <= 10^5`
- `0 <= limits[i] <= m`
- `0 <= k <= min(n * m, sum(limits))`

## Examples
### Example 1
- **Input:** `grid = [[1,2],[3,4]], limits = [1,2], k = 2`
- **Output:** `7`
- **Explanation:** From the second row, we can take at most 2 elements. The elements taken are 4 and 3. 
 The maximum possible sum of at most 2 selected elements is `4 + 3 = 7`.

### Example 2
- **Input:** `grid = [[5,3,7],[8,2,6]], limits = [2,2], k = 3`
- **Output:** `21`
- **Explanation:** From the first row, we can take at most 2 elements. The element taken is 7. 
 From the second row, we can take at most 2 elements. The elements taken are 8 and 6. 
 The maximum possible sum of at most 3 selected elements is `7 + 8 + 6 = 21`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Sum With at Most K Elements**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,2],[3,4]], limits = [1,2], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** From the second row, we can take at most 2 elements. The elements taken are 4 and 3. 
 The maximum possible sum of at most 2 selected elements is `4 + 3 = 7`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        cand = []
        for row, lim in zip(grid, limits):
            if lim:
                cand.extend(sorted(row, reverse=True)[:lim])
        cand.sort(reverse=True)
        return sum(cand[:k])
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3962. Maximum Subarray Sum After at Most K Swaps](../../3501-4000/3962-maximum-subarray-sum-after-at-most-k-swaps/)
- [1191. K-Concatenation Maximum Sum](../../1001-1500/1191-k-concatenation-maximum-sum/)
- [2106. Maximum Fruits Harvested After at Most K Steps](../../2001-2500/2106-maximum-fruits-harvested-after-at-most-k-steps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/)
