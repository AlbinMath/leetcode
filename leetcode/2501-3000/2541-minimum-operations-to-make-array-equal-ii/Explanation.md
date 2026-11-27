# LeetCode 2541: Minimum Operations to Make Array Equal II

**LeetCode Problem #2541 — Minimum Operations to Make Array Equal II**
Solve LeetCode Minimum Operations to Make Array Equal II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Make Array Equal II |
| LeetCode | #2541 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays `nums1` and `nums2` of equal length `n` and an integer `k`. You can perform the following operation on `nums1`:

Choose two indexes `i` and `j` and increment `nums1[i]` by `k` and decrement `nums1[j]` by `k`. In other words, `nums1[i] = nums1[i] + k` and `nums1[j] = nums1[j] - k`.

`nums1` is said to be **equal** to `nums2` if for all indices `i` such that `0 <= i < n`, `nums1[i] == nums2[i]`.

Return *the **minimum** number of operations required to make *`nums1`* equal to *`nums2`. If it is impossible to make them equal, return `-1`.

## Constraints
- `n == nums1.length == nums2.length`
- `2 <= n <= 10^5`
- `0 <= nums1[i], nums2[j] <= 10^9`
- `0 <= k <= 10^5`

## Examples
### Example 1
- **Input:** `nums1 = [4,3,1,4], nums2 = [1,3,7,1], k = 3`
- **Output:** `2`
- **Explanation:** In 2 operations, we can transform nums1 to nums2.
1^st operation: i = 2, j = 0. After applying the operation, nums1 = [1,3,4,4].
2^nd operation: i = 2, j = 3. After applying the operation, nums1 = [1,3,7,1].
One can prove that it is impossible to make arrays equal in fewer operations.

### Example 2
- **Input:** `nums1 = [3,8,5,2], nums2 = [2,4,1,6], k = 1`
- **Output:** `-1`
- **Explanation:** It can be proved that it is impossible to make the two arrays equal.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Operations to Make Array Equal II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [4,3,1,4], nums2 = [1,3,7,1], k = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** In 2 operations, we can transform nums1 to nums2.
1^st operation: i = 2, j = 0. After applying the operation, nums1 = [1,3,4,4].
2^nd operation: i = 2, j = 3. After applying the operation, nums1 = [1,3,7,1].
One can prove that it is impossible to make arrays equal in fewer operations.

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
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1
        pos = neg = 0
        for a, b in zip(nums1, nums2):
            d = a - b
            if d % k:
                return -1
            if d > 0:
                pos += d // k
            else:
                neg += -d // k
        return pos if pos == neg else -1
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
- [2602. Minimum Operations to Make All Array Elements Equal](../../2501-3000/2602-minimum-operations-to-make-all-array-elements-equal/)
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2654-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../2501-3000/2997-minimum-number-of-operations-to-make-array-xor-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/)
