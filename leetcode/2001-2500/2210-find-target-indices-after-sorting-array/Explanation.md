# LeetCode 2089: Find Target Indices After Sorting Array

**LeetCode Problem #2089 — Find Target Indices After Sorting Array**
Solve LeetCode Find Target Indices After Sorting Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Target Indices After Sorting Array |
| LeetCode | #2089 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` and a target element `target`.

A **target index** is an index `i` such that `nums[i] == target`.

Return *a list of the target indices of* `nums` after* sorting *`nums`* in **non-decreasing** order*. If there are no target indices, return *an **empty** list*. The returned list must be sorted in **increasing** order.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i], target <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,5,2,3], target = 2`
- **Output:** `[1,2]`
- **Explanation:** After sorting, nums is [1,

### Example 2
- **Input:** `nums = [1,2,5,2,3], target = 3`
- **Output:** `[3]`
- **Explanation:** After sorting, nums is [1,2,2,

### Example 3
- **Input:** `nums = [1,2,5,2,3], target = 5`
- **Output:** `[4]`
- **Explanation:** After sorting, nums is [1,2,2,3,

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Target Indices After Sorting Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,5,2,3], target = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2]`.
4. **Verification:** After sorting, nums is [1,

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
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less = equal = 0
        for n in nums:
            if n < target:
                less += 1
            elif n == target:
                equal += 1
        return list(range(less, less + equal))
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
- [2593. Find Score of an Array After Marking All Elements](../../2501-3000/2695-find-score-of-an-array-after-marking-all-elements/)
- [3006. Find Beautiful Indices in the Given Array I](../../3001-3500/3245-find-beautiful-indices-in-the-given-array-i/)
- [3008. Find Beautiful Indices in the Given Array II](../../3001-3500/3303-find-beautiful-indices-in-the-given-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-target-indices-after-sorting-array/)
