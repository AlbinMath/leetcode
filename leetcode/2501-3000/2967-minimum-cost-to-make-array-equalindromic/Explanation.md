# LeetCode 2967: Minimum Cost to Make Array Equalindromic

**LeetCode Problem #2967 — Minimum Cost to Make Array Equalindromic**
Solve LeetCode Minimum Cost to Make Array Equalindromic using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Make Array Equalindromic |
| LeetCode | #2967 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

In one **operation**, you may choose an index `i` and either increment or decrement `nums[i]` by 1.

Return the **minimum** number of operations required to make every element in `nums` **equal **to the **same **positive palindromic integer .

## Constraints
- `1 <= n <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `6`
- **Explanation:** Increment nums[0] twice and nums[1] once, then decrement nums[3] once and nums[4] twice. After 6 operations, nums becomes [3,3,3,3,3], and 3 is a positive palindromic integer.
It can be shown that this is the minimum number of operations required.

### Example 2
- **Input:** `nums = [10,12,13,14,15]`
- **Output:** `11`
- **Explanation:** Increment nums[0] once, then decrement nums[1], nums[2], nums[3], and nums[4] by 1, 2, 3, and 4, respectively. After 11 operations, nums becomes [11,11,11,11,11], and 11 is a positive palindromic integer.
It can be shown that this is the minimum number of operations required.

### Example 3
- **Input:** `nums = [22,33,22,33,22]`
- **Output:** `22`
- **Explanation:** Decrement nums[1] and nums[3] by 11 each. After 22 operations, nums becomes [22,22,22,22,22], and 22 is a positive palindromic integer.
It can be shown that this is the minimum number of operations required.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Cost to Make Array Equalindromic**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** Increment nums[0] twice and nums[1] once, then decrement nums[3] once and nums[4] twice. After 6 operations, nums becomes [3,3,3,3,3], and 3 is a positive palindromic integer.
It can be shown that this is the minimum number of operations required.

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
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        m = nums[n // 2]

        def mirror(left: int, odd: bool) -> int:
            s = str(left)
            return int(s + (s[-2::-1] if odd else s[::-1]))

        s = str(m)
        L = len(s)
        half = int(s[:(L + 1) // 2])
        odd = L % 2 == 1

        cands = set()
        for h in (half - 1, half, half + 1):
            if h > 0:
                cands.add(mirror(h, odd))
        # length-boundary palindromes
        cands.add(10 ** (L - 1) - 1)   # 99...9 with L-1 digits
        cands.add(10 ** L + 1)         # 100...01 with L+1 digits
        cands = {c for c in cands if c >= 1}

        def cost(x: int) -> int:
            return sum(abs(a - x) for a in nums)

        return min(cost(c) for c in cands)
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
- [2448. Minimum Cost to Make Array Equal](../../2001-2500/2448-minimum-cost-to-make-array-equal/)
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [2499. Minimum Total Cost to Make Arrays Unequal](../../2001-2500/2499-minimum-total-cost-to-make-arrays-unequal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/)
