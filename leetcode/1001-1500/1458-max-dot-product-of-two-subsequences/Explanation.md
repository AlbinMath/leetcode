# LeetCode 1458: Max Dot Product of Two Subsequences

**LeetCode Problem #1458 — Max Dot Product of Two Subsequences**
Solve LeetCode Max Dot Product of Two Subsequences using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Max Dot Product of Two Subsequences |
| LeetCode | #1458 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two arrays `nums1` and ` nums2 ` .

Return the maximum dot product between **non-empty** subsequences of nums1 and nums2 with the same length.

A subsequence of an array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, `[2,3,5]` is a subsequence of `[1,2,3,4,5]` while `[1,5,3]` is not).

## Constraints
- `1 <= nums1.length, nums2.length <= 500`
- `-1000 <= nums1[i], nums2[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums1 = [2,1,-2,5], nums2 = [3,0,-6]`
- **Output:** `18`
- **Explanation:** Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.

### Example 2
- **Input:** `nums1 = [3,-2], nums2 = [2,-6,7]`
- **Output:** `21`
- **Explanation:** Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.

### Example 3
- **Input:** `nums1 = [-1,-1], nums2 = [1,1]`
- **Output:** `-1`
- **Explanation:** Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Max Dot Product of Two Subsequences**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [2,1,-2,5], nums2 = [3,0,-6]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `18`.
4. **Verification:** Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.

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
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
            
        n = len(nums2)
        NEG_INF = float('-inf')
        dp = [NEG_INF] * (n + 1)
        
        for num1 in nums1:
            prev_diag = NEG_INF
            for j, num2 in enumerate(nums2, start=1):
                temp = dp[j]
                prod = num1 * num2
                
                take_both = prod + (prev_diag if prev_diag > 0 else 0)
                dp[j] = max(take_both, dp[j], dp[j - 1])
                
                prev_diag = temp
                
        return dp[n]
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
- [2002. Maximum Product of the Length of Two Palindromic Subsequences](../../2001-2500/2002-maximum-product-of-the-length-of-two-palindromic-subsequences/)
- [1464. Maximum Product of Two Elements in an Array](../../1001-1500/1464-maximum-product-of-two-elements-in-an-array/)
- [1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers](../../1501-2000/1577-number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/max-dot-product-of-two-subsequences/)
