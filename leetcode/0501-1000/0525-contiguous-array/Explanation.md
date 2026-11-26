# LeetCode 525: Contiguous Array

**LeetCode Problem #525 — Contiguous Array**
Solve LeetCode Contiguous Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Contiguous Array |
| LeetCode | #525 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a binary array `nums`, return *the maximum length of a contiguous subarray with an equal number of *`0`* and *`1`.

## Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `nums = [0,1]`
- **Output:** `2`
- **Explanation:** [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

### Example 2
- **Input:** `nums = [0,1,0]`
- **Output:** `2`
- **Explanation:** [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

### Example 3
- **Input:** `nums = [0,1,1,1,1,1,0,0,0]`
- **Output:** `6`
- **Explanation:** [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Contiguous Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

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
    def findMaxLength(self, nums: List[int]) -> int:
        first = {0: -1}
        s = 0
        best = 0
        for j, v in enumerate(nums):
            s += 1 if v else -1
            if s in first:
                best = max(best, j - first[s])
            else:
                first[s] = j
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
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [33. Search in Rotated Sorted Array](../../0001-0500/0033-search-in-rotated-sorted-array/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/contiguous-array/)
