# LeetCode 902: Numbers At Most N Given Digit Set

**LeetCode Problem #902 — Numbers At Most N Given Digit Set**
Solve LeetCode Numbers At Most N Given Digit Set using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Numbers At Most N Given Digit Set |
| LeetCode | #902 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of `digits` which is sorted in **non-decreasing** order. You can write numbers using each `digits[i]` as many times as we want. For example, if `digits = ['1','3','5']`, we may write numbers such as `'13'`, `'551'`, and `'1351315'`.

Return *the number of positive integers that can be generated *that are less than or equal to a given integer `n`.

## Constraints
- `1 <= digits.length <= 9`
- `digits[i].length == 1`
- `digits[i]` is a digit from `'1'` to `'9'`.
- All the values in `digits` are **unique**.
- `digits` is sorted in **non-decreasing** order.
- `1 <= n <= 10^9`

## Examples
### Example 1
- **Input:** `digits = ["1","3","5","7"], n = 100`
- **Output:** `20`
- **Explanation:** The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

### Example 2
- **Input:** `digits = ["1","4","9"], n = 1000000000`
- **Output:** `29523`
- **Explanation:** We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits array.

### Example 3
- **Input:** `digits = ["7"], n = 8`
- **Output:** `1`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Numbers At Most N Given Digit Set**, we observe the problem requirements and utilize the **Math & Logic** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `digits = ["1","3","5","7"], n = 100`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `20`.
4. **Verification:** The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

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
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        L = len(s)
        D = len(digits)

        # shorter numbers
        count = sum(D ** k for k in range(1, L))

        # same length as n
        for i, c in enumerate(s):
            smaller = sum(d < c for d in digits)
            count += smaller * D ** (L - i - 1)
            if c not in digits:
                return count   # can't keep matching n's prefix

        return count + 1       # n itself is buildable
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
- [3352. Count K-Reducible Numbers Less Than N](../../3001-3500/3352-count-k-reducible-numbers-less-than-n/)
- [2094. Finding 3-Digit Even Numbers](../../2001-2500/2094-finding-3-digit-even-numbers/)
- [2310. Sum of Numbers With Units Digit K](../../2001-2500/2310-sum-of-numbers-with-units-digit-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/)
