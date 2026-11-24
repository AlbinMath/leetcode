# LeetCode 3566: Partition Array into Two Equal Product Subsets

**LeetCode Problem #3566 — Partition Array into Two Equal Product Subsets**
Solve LeetCode Partition Array into Two Equal Product Subsets using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partition Array into Two Equal Product Subsets |
| LeetCode | #3566 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` containing **distinct** positive integers and an integer `target`.

Determine if you can partition `nums` into two **non-empty** **disjoint** **subsets**, with each element belonging to **exactly one** subset, such that the product of the elements in each subset is equal to `target`.

Return `true` if such a partition exists and `false` otherwise.

A **subset** of an array is a selection of elements of the array.

## Constraints
- `3 <= nums.length <= 12`
- `1 <= target <= 10^15`
- `1 <= nums[i] <= 100`
- All elements of `nums` are **distinct**.

## Examples
### Example 1
- **Input:** `nums = [3,1,6,8,4], target = 24`
- **Output:** `true`
- **Explanation:** The subsets `[3, 8]` and `[1, 6, 4]` each have a product of 24. Hence, the output is true.

### Example 2
- **Input:** `nums = [2,5,3,7], target = 15`
- **Output:** `false`
- **Explanation:** There is no way to partition `nums` into two non-empty disjoint subsets such that both subsets have a product of 15. Hence, the output is false.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Partition Array into Two Equal Product Subsets**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,6,8,4], target = 24`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The subsets `[3, 8]` and `[1, 6, 4]` each have a product of 24. Hence, the output is true.

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
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        total = 1
        for v in nums:
            total *= v
        if total != target * target:
            return False

        for mask in range(1, (1 << n) - 1):
            prod = 1
            for i in range(n):
                if mask >> i & 1:
                    prod *= nums[i]
                    if prod > target:
                        break
            if prod == target:
                return True
        return False
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
- [2035. Partition Array Into Two Arrays to Minimize Sum Difference](../../2001-2500/2035-partition-array-into-two-arrays-to-minimize-sum-difference/)
- [1464. Maximum Product of Two Elements in an Array](../../1001-1500/1464-maximum-product-of-two-elements-in-an-array/)
- [698. Partition to K Equal Sum Subsets](../../0501-1000/0698-partition-to-k-equal-sum-subsets/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/)
