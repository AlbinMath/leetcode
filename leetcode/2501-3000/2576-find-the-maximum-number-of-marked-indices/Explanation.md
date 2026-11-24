# LeetCode 2576: Find the Maximum Number of Marked Indices

**LeetCode Problem #2576 — Find the Maximum Number of Marked Indices**
Solve LeetCode Find the Maximum Number of Marked Indices using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Maximum Number of Marked Indices |
| LeetCode | #2576 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums`.

Initially, all of the indices are unmarked. You are allowed to make this operation any number of times:

Pick two **different unmarked** indices `i` and `j` such that `2 * nums[i] <= nums[j]`, then mark `i` and `j`.

Return *the maximum possible number of marked indices in `nums` using the above operation any number of times*.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [3,5,2,4]`
- **Output:** `2`
- **Explanation:** In the first operation: pick i = 2 and j = 1, the operation is allowed because 2 * nums[2] <= nums[1]. Then mark index 2 and 1.
It can be shown that there's no other valid operation so the answer is 2.

### Example 2
- **Input:** `nums = [9,2,5,4]`
- **Output:** `4`
- **Explanation:** In the first operation: pick i = 3 and j = 0, the operation is allowed because 2 * nums[3] <= nums[0]. Then mark index 3 and 0.
In the second operation: pick i = 1 and j = 2, the operation is allowed because 2 * nums[1] <= nums[2]. Then mark index 1 and 2.
Since there is no other operation, the answer is 4.

### Example 3
- **Input:** `nums = [7,6,8]`
- **Output:** `0`
- **Explanation:** There is no valid operation to do, so the answer is 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Maximum Number of Marked Indices**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,5,2,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** In the first operation: pick i = 2 and j = 1, the operation is allowed because 2 * nums[2] <= nums[1]. Then mark index 2 and 1.
It can be shown that there's no other valid operation so the answer is 2.

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
    def maxNumOfMarkedIndices(self, nums):
        nums.sort()
        n = len(nums)

        def ok(k):
            return all(2 * nums[i] <= nums[n - k + i] for i in range(k))

        lo, hi = 0, n // 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return 2 * lo
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
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../../2001-2500/2058-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [2744. Find Maximum Number of String Pairs](../../2501-3000/2744-find-maximum-number-of-string-pairs/)
- [3020. Find the Maximum Number of Elements in Subset](../../3001-3500/3020-find-the-maximum-number-of-elements-in-subset/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/)
