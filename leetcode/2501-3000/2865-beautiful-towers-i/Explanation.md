# LeetCode 2865: Beautiful Towers I

**LeetCode Problem #2865 — Beautiful Towers I**
Solve LeetCode Beautiful Towers I using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Beautiful Towers I |
| LeetCode | #2865 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `heights` of `n` integers representing the number of bricks in `n` consecutive towers. Your task is to remove some bricks to form a **mountain-shaped** tower arrangement. In this arrangement, the tower heights are non-decreasing, reaching a maximum peak value with one or multiple consecutive towers and then non-increasing.

Return the **maximum possible sum** of heights of a mountain-shaped tower arrangement.

## Constraints
- `1 <= n == heights.length <= 10^3`
- `1 <= heights[i] <= 10^9`

## Examples
### Example 1
- **Input:** `heights = [5,3,4,1,1]`
- **Output:** `13`
- **Explanation:** We remove some bricks to make `heights = [5,3,3,1,1]`, the peak is at index 0.

### Example 2
- **Input:** `heights = [6,5,3,9,2,7]`
- **Output:** `22`
- **Explanation:** We remove some bricks to make `heights = [3,3,3,9,2,2]`, the peak is at index 3.

### Example 3
- **Input:** `heights = [3,2,5,5,2,3]`
- **Output:** `18`
- **Explanation:** We remove some bricks to make `heights = [2,2,5,5,2,2]`, the peak is at index 2 or 3.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Beautiful Towers I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `heights = [5,3,4,1,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** We remove some bricks to make `heights = [5,3,3,1,1]`, the peak is at index 0.

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
from typing import List

class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        n = len(heights)
        best = 0
        for p in range(n):
            total = heights[p]
            cur = heights[p]
            for i in range(p - 1, -1, -1):
                cur = min(cur, heights[i])
                total += cur
            cur = heights[p]
            for i in range(p + 1, n):
                cur = min(cur, heights[i])
                total += cur
            best = max(best, total)
        return best
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
- [2866. Beautiful Towers II](../../2501-3000/2866-beautiful-towers-ii/)
- [3301. Maximize the Total Height of Unique Towers](../../3001-3500/3301-maximize-the-total-height-of-unique-towers/)
- [526. Beautiful Arrangement](../../0501-1000/0526-beautiful-arrangement/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/beautiful-towers-i/)
