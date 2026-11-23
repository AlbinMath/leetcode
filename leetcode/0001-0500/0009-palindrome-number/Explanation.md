# LeetCode 9: Palindrome Number

**LeetCode Problem #9 — Palindrome Number**
Solve LeetCode Palindrome Number using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Palindrome Number |
| LeetCode | #9 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `x`, return `true` if `x` is a **palindrome** , and `false` otherwise.

## Constraints
- `-2^31 <= x <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `x = 121`
- **Output:** `true`
- **Explanation:** 121 reads as 121 from left to right and from right to left.

### Example 2
- **Input:** `x = -121`
- **Output:** `false`
- **Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

### Example 3
- **Input:** `x = 10`
- **Output:** `false`
- **Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
If the number is negative, it cannot be a palindrome (due to the minus sign), so we return `False`.
We store the `original` number and create a `reversed_num` variable initialized to `0`.
Using a `while` loop, we extract the last digit of the number using modulo 10 (`x % 10`) and append it to `reversed_num` by multiplying the current `reversed_num` by 10 and adding the digit.
Then, we remove the last digit from `x` using integer division (`x //= 10`).
Finally, we check if the `original` number is equal to the `reversed_num`.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `x = 121`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** 121 reads as 121 from left to right and from right to left.

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
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        r = 0
        while x > r:
            r = r * 10 + x % 10
            x //= 10
        return x == r or x == r // 10
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
- [2193. Minimum Number of Moves to Make Palindrome](../../1001-1500/1356-minimum-number-of-moves-to-make-palindrome/)
- [2472. Maximum Number of Non-overlapping Palindrome Substrings](../../2501-3000/2559-maximum-number-of-non-overlapping-palindrome-substrings/)
- [3646. Next Special Palindrome Number](../../3501-4000/3951-next-special-palindrome-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/palindrome-number/)
