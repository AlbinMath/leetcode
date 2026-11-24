# LeetCode 2439: Minimize Maximum of Array

**LeetCode Problem #2439 — Minimize Maximum of Array**
Solve LeetCode Minimize Maximum of Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimize Maximum of Array |
| LeetCode | #2439 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** array `nums` comprising of `n` non-negative integers.

In one operation, you must:

Choose an integer `i` such that `1 <= i < n` and `nums[i] > 0`. 
 Decrease `nums[i]` by 1. 
 Increase `nums[i - 1]` by 1.

Return* the **minimum** possible value of the **maximum** integer of *`nums`* after performing **any** number of operations*.

## Constraints
- `n == nums.length`
- `2 <= n <= 10^5`
- `0 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [3,7,1,6]`
- **Output:** `5`
- **Explanation:** One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
Therefore, we return 5.

### Example 2
- **Input:** `nums = [10,1]`
- **Output:** `10`
- **Explanation:** It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimize Maximum of Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,7,1,6]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
Therefore, we return 5.

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
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        total = 0
        for i, x in enumerate(nums, 1):
            total += x
            ans = max(ans, (total + i - 1) // i)
        return ans
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
- [4098. Minimize the Maximum Value of GCD-Connected Array](../../4001-4500/4098-minimize-the-maximum-value-of-gcd-connected-array/)
- [421. Maximum XOR of Two Numbers in an Array](../../0001-0500/0421-maximum-xor-of-two-numbers-in-an-array/)
- [1464. Maximum Product of Two Elements in an Array](../../1001-1500/1464-maximum-product-of-two-elements-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimize-maximum-of-array/)
