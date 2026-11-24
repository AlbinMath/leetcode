# LeetCode 3132: Find the Integer Added to Array II

**LeetCode Problem #3132 — Find the Integer Added to Array II**
Solve LeetCode Find the Integer Added to Array II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Integer Added to Array II |
| LeetCode | #3132 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays `nums1` and `nums2`.

We say that `nums2` is reachable from `nums1` with an integer `x` if there exist two elements in `nums1` that, when removed, and `x` is added to all the remaining elements of `nums1` (or subtracted in the case of a negative `x`), the resulting array becomes equal to `nums2`. Two arrays are considered **equal** when they contain the same integers with the same frequencies.

Return the **minimum** possible integer `x` that makes `nums2` reachable from `nums1`.

It is guaranteed that `nums2` is reachable from `nums1` with at least one `x`.

## Constraints
- `3 <= nums1.length <= 200`
- `nums2.length == nums1.length - 2`
- `0 <= nums1[i], nums2[i] <= 1000`
- It is guaranteed that `nums2` is reachable from `nums1` with at least one `x`.

## Examples
### Example 1
- **Input:** `nums1 = [4,20,16,12,8], nums2 = [14,18,10]`
- **Output:** `-2`
- **Explanation:** After removing elements at indices `[0,4]` and adding -2, `nums1` becomes `[18,14,10]`.

### Example 2
- **Input:** `nums1 = [3,5,5,3], nums2 = [7,7]`
- **Output:** `2`
- **Explanation:** After removing elements at indices `[0,3]` and adding 2, `nums1` becomes `[7,7]`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Integer Added to Array II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [4,20,16,12,8], nums2 = [14,18,10]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `-2`.
4. **Verification:** After removing elements at indices `[0,4]` and adding -2, `nums1` becomes `[18,14,10]`.

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
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        ans = float('inf')

        for i in range(3):
            x = nums2[0] - nums1[i]
            j = 0
            for v in nums1:
                if j < len(nums2) and v + x == nums2[j]:
                    j += 1
            if j == len(nums2):
                ans = min(ans, x)

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
- [1394. Find Lucky Integer in an Array](../../1001-1500/1394-find-lucky-integer-in-an-array/)
- [1985. Find the Kth Largest Integer in the Array](../../1501-2000/1985-find-the-kth-largest-integer-in-the-array/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-integer-added-to-array-ii/)
