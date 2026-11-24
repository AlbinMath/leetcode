# LeetCode 866: Prime Palindrome

**LeetCode Problem #866 — Prime Palindrome**
Solve LeetCode Prime Palindrome using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Prime Palindrome |
| LeetCode | #866 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer n, return *the smallest **prime palindrome** greater than or equal to *`n`.

An integer is **prime** if it has exactly two divisors: `1` and itself. Note that `1` is not a prime number.

For example, `2`, `3`, `5`, `7`, `11`, and `13` are all primes.

An integer is a **palindrome** if it reads the same from left to right as it does from right to left.

For example, `101` and `12321` are palindromes.

The test cases are generated so that the answer always exists and is in the range `[2, 2 * 10^8]`.

## Constraints
- `1 <= n <= 10^8`

## Examples
### Example 1
- **Input:** `n = 6`
- **Output:** `7`

### Example 2
- **Input:** `n = 8`
- **Output:** `11`

### Example 3
- **Input:** `n = 13`
- **Output:** `101`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Prime Palindrome**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 6`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.

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
    def primePalindrome(self, n: int) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        if 8 <= n <= 11:
            return 11  # the only even-length prime palindrome

        for root in range(1, 10 ** 5):
            s = str(root)
            p = int(s + s[-2::-1])  # odd-length palindrome, middle digit not repeated
            if p >= n and is_prime(p):
                return p
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
- [762. Prime Number of Set Bits in Binary Representation](../../0501-1000/0762-prime-number-of-set-bits-in-binary-representation/)
- [786. K-th Smallest Prime Fraction](../../0501-1000/0786-k-th-smallest-prime-fraction/)
- [1175. Prime Arrangements](../../1001-1500/1175-prime-arrangements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/prime-palindrome/)
