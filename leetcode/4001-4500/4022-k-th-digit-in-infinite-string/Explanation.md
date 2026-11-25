# LeetCode 4022: K-th Digit in Infinite String

**LeetCode Problem #4022 — K-th Digit in Infinite String**
Solve LeetCode K-th Digit in Infinite String using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | K-th Digit in Infinite String |
| LeetCode | #4022 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `k`.

An **infinite** string is formed by **concatenating** the **decimal** representations of the **positive** integers, without separators.

For every nonnegative integer `b`, block `b` contains the **positive** integers from `10 * b` through `10 * b + 9`. The integers in each block are appended as follows:

If `b` is even, append the integers in **increasing** order. 
 If `b` is odd, append the integers in **decreasing** order.

Therefore, the string starts with the integers 1 through 9, followed by 19 through 10, then 20 through 29, then 39 through 30, and so on.

Return the `k^th` digit (1-indexed) of this string.

## Constraints
- `1 <= k <= 10^15`

## Examples
### Example 1
- **Input:** `k = 4`
- **Output:** `4`
- **Explanation:** The string begins as `"123 4 56789.."`. The 4^th digit is `'4'`.

### Example 2
- **Input:** `k = 15`
- **Output:** `7`
- **Explanation:** The string begins as `"12345678919181 7 .."`. The 15^th digit is `'7'`.

### Example 3
- **Input:** `k = 11`
- **Output:** `9`
- **Explanation:** The string begins as `"1234567891 9 .."`. The 11^th digit is `'9'`.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **K-th Digit in Infinite String**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `k = 4`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The string begins as `"123 4 56789.."`. The 4^th digit is `'4'`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def kthDigit(self, k: int) -> int:
        if k <= 9:
            return k
        k -= 9
        d = 2
        while True:
            nblocks = 9 * 10 ** (d - 2)
            total = nblocks * 10 * d
            if k > total:
                k -= total
                d += 1
            else:
                break
        blk, off = divmod(k - 1, 10 * d)
        b = 10 ** (d - 2) + blk
        pos, ch = divmod(off, d)
        num = 10 * b + pos if b % 2 == 0 else 10 * b + 9 - pos
        return int(str(num)[ch])
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1415. The k-th Lexicographical String of All Happy Strings of Length n](../../1001-1500/1415-the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)
- [3304. Find the K-th Character in String Game I](../../3001-3500/3304-find-the-k-th-character-in-string-game-i/)
- [3307. Find the K-th Character in String Game II](../../3001-3500/3307-find-the-k-th-character-in-string-game-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/k-th-digit-in-infinite-string/)
