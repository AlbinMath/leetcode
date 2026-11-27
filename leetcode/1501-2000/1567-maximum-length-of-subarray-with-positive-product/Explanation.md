# LeetCode 1567: Maximum Length of Subarray With Positive Product

**LeetCode Problem #1567 — Maximum Length of Subarray With Positive Product**
Solve LeetCode Maximum Length of Subarray With Positive Product using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Length of Subarray With Positive Product |
| LeetCode | #1567 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of integers `nums`, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return *the maximum length of a subarray with positive product*.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,-2,-3,4]`
- **Output:** `4`
- **Explanation:** The array nums already has a positive product of 24.

### Example 2
- **Input:** `nums = [0,1,-2,-3,-4]`
- **Output:** `3`
- **Explanation:** The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.

### Example 3
- **Input:** `nums = [-1,-2,-3,0,1]`
- **Output:** `2`
- **Explanation:** The longest subarray with positive product is [-1,-2] or [-2,-3].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Length of Subarray With Positive Product**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,-2,-3,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The array nums already has a positive product of 24.

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
    def getMaxLen(self, nums: List[int]) -> int:
        pos = neg = 0
        ans = 0
        for x in nums:
            if x > 0:
                pos, neg = pos + 1, (neg + 1 if neg > 0 else 0)
            elif x < 0:
                pos, neg = (neg + 1 if neg > 0 else 0), pos + 1
            else:
                pos = neg = 0
            ans = max(ans, pos)
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
- [152. Maximum Product Subarray](../../0001-0500/0152-maximum-product-subarray/)
- [718. Maximum Length of Repeated Subarray](../../0501-1000/0718-maximum-length-of-repeated-subarray/)
- [1856. Maximum Subarray Min-Product](../../1501-2000/1856-maximum-subarray-min-product/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/)
