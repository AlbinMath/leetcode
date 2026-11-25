# LeetCode 1695: Maximum Erasure Value

**LeetCode Problem #1695 — Maximum Erasure Value**
Solve LeetCode Maximum Erasure Value using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Erasure Value |
| LeetCode | #1695 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of positive integers `nums` and want to erase a subarray containing **unique elements**. The **score** you get by erasing the subarray is equal to the **sum** of its elements.

Return *the **maximum score** you can get by erasing **exactly one** subarray.*

An array `b` is called to be a subarray of `a` if it forms a contiguous subsequence of `a`, that is, if it is equal to `a[l],a[l+1],...,a[r]` for some `(l,r)`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [4,2,4,5,6]`
- **Output:** `17`
- **Explanation:** The optimal subarray here is [2,4,5,6].

### Example 2
- **Input:** `nums = [5,2,1,2,5,2,1,2,5]`
- **Output:** `8`
- **Explanation:** The optimal subarray here is [5,2,1] or [1,2,5].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Erasure Value**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,2,4,5,6]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `17`.
4. **Verification:** The optimal subarray here is [2,4,5,6].

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
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        curr_sum = 0
        max_sum = 0
        
        for val in nums:
            while val in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            seen.add(val)
            curr_sum += val
            if curr_sum > max_sum:
                max_sum = curr_sum
                
        return max_sum
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
- [1802. Maximum Value at a Given Index in a Bounded Array](../../1501-2000/1802-maximum-value-at-a-given-index-in-a-bounded-array/)
- [1881. Maximum Value after Insertion](../../1501-2000/1881-maximum-value-after-insertion/)
- [2218. Maximum Value of K Coins From Piles](../../2001-2500/2218-maximum-value-of-k-coins-from-piles/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-erasure-value/)
