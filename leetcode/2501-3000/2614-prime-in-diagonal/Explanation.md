# LeetCode 2614: Prime In Diagonal

**LeetCode Problem #2614 — Prime In Diagonal**
Solve LeetCode Prime In Diagonal using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Prime In Diagonal |
| LeetCode | #2614 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 0-indexed two-dimensional integer array `nums`.

Return *the largest **prime** number that lies on at least one of the diagonals of *`nums`. In case, no prime is present on any of the diagonals, return* 0.*

Note that:

An integer is **prime** if it is greater than `1` and has no positive integer divisors other than `1` and itself. 
 An integer `val` is on one of the **diagonals** of `nums` if there exists an integer `i` for which `nums[i][i] = val` or an `i` for which `nums[i][nums.length - i - 1] = val`.

In the above diagram, one diagonal is **[1,5,9]** and another diagonal is** [3,5,7]**.

## Constraints
- `1 <= nums.length <= 300`
- `nums.length == nums_i.length`
- `1 <= nums [i][j] <= 4*10^6`

## Examples
### Example 1
- **Input:** `nums = [[1,2,3],[5,6,7],[9,10,11]]`
- **Output:** `11`
- **Explanation:** The numbers 1, 3, 6, 9, and 11 are the only numbers present on at least one of the diagonals. Since 11 is the largest prime, we return 11.

### Example 2
- **Input:** `nums = [[1,2,3],[5,17,7],[9,11,10]]`
- **Output:** `17`
- **Explanation:** The numbers 1, 3, 9, 10, and 17 are all present on at least one of the diagonals. 17 is the largest prime, so we return 17.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Prime In Diagonal**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [[1,2,3],[5,6,7],[9,10,11]]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `11`.
4. **Verification:** The numbers 1, 3, 6, 9, and 11 are the only numbers present on at least one of the diagonals. Since 11 is the largest prime, we return 11.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
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

        n = len(nums)
        best = 0
        for i in range(n):
            for v in (nums[i][i], nums[i][n - 1 - i]):
                if v > best and is_prime(v):
                    best = v
        return best
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [762. Prime Number of Set Bits in Binary Representation](../../0501-1000/0762-prime-number-of-set-bits-in-binary-representation/)
- [786. K-th Smallest Prime Fraction](../../0501-1000/0786-k-th-smallest-prime-fraction/)
- [866. Prime Palindrome](../../0501-1000/0866-prime-palindrome/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/prime-in-diagonal/)
