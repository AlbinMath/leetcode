# LeetCode 479: Largest Palindrome Product

**LeetCode Problem #479 — Largest Palindrome Product**
Solve LeetCode Largest Palindrome Product using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Palindrome Product |
| LeetCode | #479 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer n, return *the **largest palindromic integer** that can be represented as the product of two `n`-digits integers*. Since the answer can be very large, return it **modulo** `1337`.

## Constraints
- `1 <= n <= 8`

## Examples
### Example 1
- **Input:** `n = 2`
- **Output:** `987`

### Example 2
- **Input:** `n = 1`
- **Output:** `9`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Largest Palindrome Product**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `987`.

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
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        hi = 10 ** n - 1
        lo = 10 ** (n - 1)
        for h in range(hi, lo - 1, -1):
            s = str(h)
            p = int(s + s[::-1])
            x = hi
            while x * x >= p:
                if p % x == 0:
                    return p % 1337
                x -= 1
        return -1
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
- [3260. Find the Largest Palindrome Divisible by K](../../3501-4000/3552-find-the-largest-palindrome-divisible-by-k/)
- [84. Largest Rectangle in Histogram](../../0001-0500/0084-largest-rectangle-in-histogram/)
- [179. Largest Number](../../0001-0500/0179-largest-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-palindrome-product/)
