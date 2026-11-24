# LeetCode 1775: Equal Sum Arrays With Minimum Number of Operations

**LeetCode Problem #1775 — Equal Sum Arrays With Minimum Number of Operations**
Solve LeetCode Equal Sum Arrays With Minimum Number of Operations using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Equal Sum Arrays With Minimum Number of Operations |
| LeetCode | #1775 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two arrays of integers `nums1` and ` nums2 `, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer's value in **any **of the arrays to **any** value between 1 and 6, inclusive.

Return the **minimum** number of operations required to make the sum of values in `nums1` equal to the sum of values in `nums2`. Return -1​​​​​ if it is not possible to make the sum of the two arrays **equal**.

## Constraints
- `1 <= nums1.length, nums2.length <= 10^5`
- `1 <= nums1[i], nums2[i] <= 6`

## Examples
### Example 1
- **Input:** `nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]`
- **Output:** `3`
- **Explanation:** You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [

### Example 2
- **Input:** `nums1 = [1,1,1,1,1,1,1], nums2 = [6]`
- **Output:** `-1`
- **Explanation:** There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.

### Example 3
- **Input:** `nums1 = [6,6], nums2 = [1]`
- **Output:** `3`
- **Explanation:** You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed. 
- Change nums1[0] to 2. nums1 = [

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Equal Sum Arrays With Minimum Number of Operations**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0
        if s1 > s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1
        diff = s2 - s1

        gains = [0] * 6
        for x in nums1:
            gains[6 - x] += 1      # raise to 6
        for y in nums2:
            gains[y - 1] += 1      # lower to 1

        ops = 0
        for g in range(5, 0, -1):
            if diff <= 0:
                break
            # number of ops with gain g needed, capped by availability
            need = (diff + g - 1) // g
            use = min(need, gains[g])
            ops += use
            diff -= use * g
        return ops if diff <= 0 else -1
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2654-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../2501-3000/2997-minimum-number-of-operations-to-make-array-xor-equal-to-k/)
- [2998. Minimum Number of Operations to Make X and Y Equal](../../2501-3000/2998-minimum-number-of-operations-to-make-x-and-y-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/)
