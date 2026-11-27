# LeetCode 870: Advantage Shuffle

**LeetCode Problem #870 — Advantage Shuffle**
Solve LeetCode Advantage Shuffle using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Advantage Shuffle |
| LeetCode | #870 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays `nums1` and `nums2` both of the same length. The **advantage** of `nums1` with respect to `nums2` is the number of indices `i` for which `nums1[i] > nums2[i]`.

Return *any permutation of *`nums1`* that maximizes its **advantage** with respect to *`nums2`.

## Constraints
- `1 <= nums1.length <= 10^5`
- `nums2.length == nums1.length`
- `0 <= nums1[i], nums2[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums1 = [2,7,11,15], nums2 = [1,10,4,11]`
- **Output:** `[2,11,7,15]`

### Example 2
- **Input:** `nums1 = [12,24,8,32], nums2 = [13,25,32,11]`
- **Output:** `[24,32,8,12]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Advantage Shuffle**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [2,7,11,15], nums2 = [1,10,4,11]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,11,7,15]`.

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
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort()
        idx = sorted(range(n), key=lambda i: nums2[i])  # indices of nums2 by value
        res = [0] * n
        lo, hi = 0, n - 1  # pointers into sorted nums1
        # process nums2 from largest to smallest
        for i in reversed(idx):
            if nums1[hi] > nums2[i]:
                res[i] = nums1[hi]
                hi -= 1
            else:
                res[i] = nums1[lo]
                lo += 1
        return res
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
- [384. Shuffle an Array](../../0001-0500/0384-shuffle-an-array/)
- [1470. Shuffle the Array](../../1001-1500/1470-shuffle-the-array/)
- [1528. Shuffle String](../../1501-2000/1528-shuffle-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/advantage-shuffle/)
