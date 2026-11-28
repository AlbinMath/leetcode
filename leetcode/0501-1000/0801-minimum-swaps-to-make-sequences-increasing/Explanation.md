# LeetCode 801: Minimum Swaps To Make Sequences Increasing

**LeetCode Problem #801 — Minimum Swaps To Make Sequences Increasing**
Solve LeetCode Minimum Swaps To Make Sequences Increasing using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Swaps To Make Sequences Increasing |
| LeetCode | #801 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays of the same length `nums1` and `nums2`. In one operation, you are allowed to swap `nums1[i]` with `nums2[i]`.

For example, if `nums1 = [1,2,3, 8 ]`, and `nums2 = [5,6,7, 4 ]`, you can swap the element at `i = 3` to obtain `nums1 = [1,2,3,4]` and `nums2 = [5,6,7,8]`.

Return *the minimum number of needed operations to make *`nums1`* and *`nums2`* **strictly increasing***. The test cases are generated so that the given input always makes it possible.

An array `arr` is **strictly increasing** if and only if `arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1]`.

## Constraints
- `2 <= nums1.length <= 10^5`
- `nums2.length == nums1.length`
- `0 <= nums1[i], nums2[i] <= 2 * 10^5`

## Examples
### Example 1
- **Input:** `nums1 = [1,3,5,4], nums2 = [1,2,3,7]`
- **Output:** `1`
- **Explanation:** Swap nums1[3] and nums2[3]. Then the sequences are:
nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
which are both strictly increasing.

### Example 2
- **Input:** `nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]`
- **Output:** `1`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Swaps To Make Sequences Increasing**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,3,5,4], nums2 = [1,2,3,7]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Swap nums1[3] and nums2[3]. Then the sequences are:
nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
which are both strictly increasing.

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
    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        keep, swap = 0, 1
        
        for i in range(1, n):
            next_keep = next_swap = float('inf')
            if nums1[i - 1] < nums1[i] and nums2[i - 1] < nums2[i]:
                next_keep = min(next_keep, keep)
                next_swap = min(next_swap, swap + 1)
            if nums1[i - 1] < nums2[i] and nums2[i - 1] < nums1[i]:
                next_keep = min(next_keep, swap)
                next_swap = min(next_swap, keep + 1)
                
            keep, swap = next_keep, next_swap
            
        return min(keep, swap)
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
- [1247. Minimum Swaps to Make Strings Equal](../../1001-1500/1247-minimum-swaps-to-make-strings-equal/)
- [1864. Minimum Number of Swaps to Make the Binary String Alternating](../../1501-2000/1864-minimum-number-of-swaps-to-make-the-binary-string-alternating/)
- [1963. Minimum Number of Swaps to Make the String Balanced](../../1501-2000/1963-minimum-number-of-swaps-to-make-the-string-balanced/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/)
