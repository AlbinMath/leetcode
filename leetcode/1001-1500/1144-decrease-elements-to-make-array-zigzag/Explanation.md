# LeetCode 1144: Decrease Elements To Make Array Zigzag

**LeetCode Problem #1144 — Decrease Elements To Make Array Zigzag**
Solve LeetCode Decrease Elements To Make Array Zigzag using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Decrease Elements To Make Array Zigzag |
| LeetCode | #1144 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `nums` of integers, a *move* consists of choosing any element and **decreasing it by 1**.

An array `A` is a *zigzag array* if either:

Every even-indexed element is greater than adjacent elements, ie. `A[0] > A[1] < A[2] > A[3] < A[4] > ...` 
 OR, every odd-indexed element is greater than adjacent elements, ie. `A[0] < A[1] > A[2] < A[3] > A[4] < ...`

Return the minimum number of moves to transform the given array `nums` into a zigzag array.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [1,2,3]`
- **Output:** `2`
- **Explanation:** We can decrease 2 to 0 or 3 to 1.

### Example 2
- **Input:** `nums = [9,6,1,6,2]`
- **Output:** `4`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Decrease Elements To Make Array Zigzag**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can decrease 2 to 0 or 3 to 1.

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
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        INF = float('inf')

        def cost(start: int) -> int:
            # valleys are at indices start, start+2, ...
            total = 0
            for i in range(start, n, 2):
                left = nums[i - 1] if i > 0 else INF
                right = nums[i + 1] if i + 1 < n else INF
                m = min(left, right)
                if nums[i] >= m:
                    total += nums[i] - m + 1
            return total

        return min(cost(0), cost(1))
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
- [1887. Reduction Operations to Make the Array Elements Equal](../../1501-2000/1887-reduction-operations-to-make-the-array-elements-equal/)
- [2602. Minimum Operations to Make All Array Elements Equal](../../2501-3000/2602-minimum-operations-to-make-all-array-elements-equal/)
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2654-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/)
