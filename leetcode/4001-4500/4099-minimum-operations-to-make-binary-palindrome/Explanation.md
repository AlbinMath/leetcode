# LeetCode 3766: Minimum Operations to Make Binary Palindrome

**LeetCode Problem #3766 — Minimum Operations to Make Binary Palindrome**
Solve LeetCode Minimum Operations to Make Binary Palindrome using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Make Binary Palindrome |
| LeetCode | #3766 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

For each element `nums[i]`, you may perform the following operations **any** number of times (including zero):

Increase `nums[i]` by 1, or 
 Decrease `nums[i]` by 1.

A number is called a **binary palindrome** if its binary representation without leading zeros reads the same forward and backward.

Your task is to return an integer array `ans`, where `ans[i]` represents the **minimum** number of operations required to convert `nums[i]` into a **binary palindrome**.

## Constraints
- `1 <= nums.length <= 5000`
- `^​​​​​​​1 <= nums[i] <=^ 5000`

## Examples
### Example 1
- **Input:** `nums = [1,2,4]`
- **Output:** `[0,1,1]`
- **Explanation:** One optimal set of operations: 

 
 
 
 `nums[i]` 
 Binary(`nums[i]`) 
 Nearest 
 Palindrome 
 Binary 
 (Palindrome) 
 Operations Required 
 `ans[i]` 
 
 
 
 
 1 
 1 
 1 
 1 
 Already palindrome 
 0 
 
 
 2 
 10 
 3 
 11 
 Increase by 1 
 1 
 
 
 4 
 100 
 3 
 11 
 Decrease by 1 
 1 
 
 
 

 Thus, `ans = [0, 1, 1]`.

### Example 2
- **Input:** `nums = [6,7,12]`
- **Output:** `[1,0,3]`
- **Explanation:** One optimal set of operations: 

 
 
 
 `nums[i]` 
 Binary(`nums[i]`) 
 Nearest 
 Palindrome 
 Binary 
 (Palindrome) 
 Operations Required 
 `ans[i]` 
 
 
 
 
 6 
 110 
 5 
 101 
 Decrease by 1 
 1 
 
 
 7 
 111 
 7 
 111 
 Already palindrome 
 0 
 
 
 12 
 1100 
 15 
 1111 
 Increase by 3 
 3 
 
 
 

 Thus, `ans = [1, 0, 3]`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Operations to Make Binary Palindrome**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,4]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,1,1]`.
4. **Verification:** One optimal set of operations: 

 
 
 
 `nums[i]` 
 Binary(`nums[i]`) 
 Nearest 
 Palindrome 
 Binary 
 (Palindrome) 
 Operations Required 
 `ans[i]` 
 
 
 
 
 1 
 1 
 1 
 1 
 Already palindrome 
 0 
 
 
 2 
 10 
 3 
 11 
 Increase by 1 
 1 
 
 
 4 
 100 
 3 
 11 
 Decrease by 1 
 1 
 
 
 

 Thus, `ans = [0, 1, 1]`.

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
from bisect import bisect_left

class Solution(object):
    def minOperations(self, nums):
        pals = []
        for v in range(1, 8193):
            b = bin(v)[2:]
            if b == b[::-1]:
                pals.append(v)

        res = []
        for x in nums:
            i = bisect_left(pals, x)
            best = abs(pals[i] - x)           # smallest palindrome >= x
            if i > 0:
                best = min(best, x - pals[i - 1])  # largest palindrome < x
            res.append(best)
        return res
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
- [3191. Minimum Operations to Make Binary Array Elements Equal to One I](../../3001-3500/3475-minimum-operations-to-make-binary-array-elements-equal-to-one-i/)
- [4021. Minimum Operations to Make a Rotated Palindrome I](../../4001-4500/4350-minimum-operations-to-make-a-rotated-palindrome-i/)
- [1312. Minimum Insertion Steps to Make a String Palindrome](../../1001-1500/1437-minimum-insertion-steps-to-make-a-string-palindrome/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/)
