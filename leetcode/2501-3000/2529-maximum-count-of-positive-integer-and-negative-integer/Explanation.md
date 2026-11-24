# LeetCode 2529: Maximum Count of Positive Integer and Negative Integer

**LeetCode Problem #2529 — Maximum Count of Positive Integer and Negative Integer**
Solve LeetCode Maximum Count of Positive Integer and Negative Integer using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Count of Positive Integer and Negative Integer |
| LeetCode | #2529 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `nums` sorted in **non-decreasing** order, return *the maximum between the number of positive integers and the number of negative integers.*

In other words, if the number of positive integers in `nums` is `pos` and the number of negative integers is `neg`, then return the maximum of `pos` and `neg`.

**Note** that `0` is neither positive nor negative.

## Constraints
- `1 <= nums.length <= 2000`
- `-2000 <= nums[i] <= 2000`
- `nums` is sorted in a **non-decreasing order**.

## Examples
### Example 1
- **Input:** `nums = [-2,-1,-1,1,2,3]`
- **Output:** `3`
- **Explanation:** There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

### Example 2
- **Input:** `nums = [-3,-2,-1,0,0,1,2]`
- **Output:** `3`
- **Explanation:** There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

### Example 3
- **Input:** `nums = [5,20,66,1314]`
- **Output:** `4`
- **Explanation:** There are 4 positive integers and 0 negative integers. The maximum count among them is 4.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Maximum Count of Positive Integer and Negative Integer**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [-2,-1,-1,1,2,3]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from bisect import bisect_left, bisect_right

class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        neg = bisect_left(nums, 0)
        pos = len(nums) - bisect_right(nums, 0)
        
        return max(neg, pos)
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [2044. Count Number of Maximum Bitwise-OR Subsets](../../2001-2500/2044-count-number-of-maximum-bitwise-or-subsets/)
- [2178. Maximum Split of Positive Even Integers](../../2001-2500/2178-maximum-split-of-positive-even-integers/)
- [2842. Count K-Subsequences of a String With Maximum Beauty](../../2501-3000/2842-count-k-subsequences-of-a-string-with-maximum-beauty/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/)
